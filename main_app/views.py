from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId
import numpy as np
from PIL import Image
import io, base64
from .utils.predict import predict_image
from datetime import datetime


# ---- Hàm trả về collection trong MongoDB ----
def get_history_collection():
    client = MongoClient(settings.MONGO_URI)
    db = client["history"]   # 👈 DB name (m nhớ tạo trong Mongo Atlas)
    return db["prediction_history"]  # 👈 Collection name


def image_to_list(file):
    img = Image.open(file).convert("RGB")
    return np.array(img).tolist()


def list_to_base64(img_list):
    img = Image.fromarray(np.array(img_list, dtype=np.uint8))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")


@login_required
def dashboard_view(request):
    history_col = get_history_collection()   # 👈 chỉ connect khi cần

    if request.method == "POST":
        action = request.POST.get("action")

        # --- Xóa 1 record trong lịch sử ---
        if action == "delete_one":
            record_id = request.POST.get("record_id")
            if record_id:
                history_col.delete_one({
                    "_id": ObjectId(record_id),
                    "user_id": request.user.id
                })
            return redirect("main_app:dashboard")

        uploaded_file = None

        # --- 1. Nếu upload file từ máy ---
        if request.FILES.get("image"):
            uploaded_file = request.FILES["image"]

        # --- 2. Nếu chụp ảnh từ camera (base64) ---
        elif request.POST.get("captured_image"):
            data_url = request.POST["captured_image"]
            try:
                header, encoded = data_url.split(";base64,")
                img_data = base64.b64decode(encoded)

                uploaded_file = io.BytesIO(img_data)
                uploaded_file.name = "camera_capture.png"
            except Exception as e:
                print("❌ Lỗi decode base64:", e)

        # --- Nếu có ảnh (dù từ file hay camera) ---
        if uploaded_file:
            img_list = image_to_list(uploaded_file)

            uploaded_file.seek(0)
            img_bytes = io.BytesIO(
                uploaded_file.read() if hasattr(uploaded_file, "read") else uploaded_file.getvalue()
            )

            predicted_class, prob = predict_image(img_bytes)

            history_col.insert_one({
                "user_id": request.user.id,
                "image_list": img_list,
                "predicted_class": predicted_class,
                "probability": float(prob * 100),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            return redirect("main_app:dashboard")

    # --- GET: load dashboard + history ---
    history_docs = history_col.find({"user_id": request.user.id}).sort("_id", -1)

    history_list = []
    for doc in history_docs:
        base64_img = list_to_base64(doc["image_list"])
        history_list.append({
            "id": str(doc["_id"]),
            "predicted_class": doc["predicted_class"],
            "probability": doc["probability"],
            "image_base64": base64_img,
            "created_at": doc.get("created_at", "")
        })

    return render(request, "main_app/dashboard.html", {
        "history_list": history_list
    })









