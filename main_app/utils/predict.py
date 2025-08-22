import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

# --- Đường dẫn tới model ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "utils", "leaf_disease_model.h5")

# --- Load model ---
model = keras.models.load_model(MODEL_PATH, compile=False)

# --- Load labels ---
LABELS_PATH = os.path.join(BASE_DIR, "utils", "labels.txt")
if os.path.exists(LABELS_PATH):
    with open(LABELS_PATH, "r") as f:
        class_names = [line.strip() for line in f.readlines()]
else:
    class_names = ["healthy", "bo_tri", "vang_la"]


# --- Hàm dự đoán ---
def predict_image(img_input):
    try:
        # img_input có thể là path hoặc BytesIO
        img = keras.utils.load_img(img_input, target_size=(224, 224))
        img_array = keras.utils.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_index]
        probability = float(np.max(predictions[0]))

        return predicted_class, probability

    except Exception as e:
        print("❌ Lỗi khi dự đoán:", e)
        return "error", 0.0
