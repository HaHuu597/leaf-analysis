from django.shortcuts import render, redirect   # render: trả về HTML, redirect: chuyển hướng
from django.contrib.auth import login, logout   # login: đăng nhập user, logout: đăng xuất user
from django.contrib import messages             # messages: dùng để hiển thị thông báo
from .forms import SignUpForm, LoginForm        # import form đăng ký và đăng nhập


# ---------------- Trang chủ ----------------
def home(request):
    # Chỉ cần hiển thị trang home.html
    return render(request, "home.html")


# ---------------- Đăng ký ----------------
def signup_view(request):
    if request.method == "POST":   # Nếu người dùng bấm nút đăng ký (gửi form)
        form = SignUpForm(request.POST)  # Lấy dữ liệu từ form
        if form.is_valid():        # Nếu form hợp lệ
            user = form.save()     # Lưu user mới vào database
            login(request, user)   # Đăng nhập ngay sau khi đăng ký
            messages.success(request, "Đăng ký thành công!")  # Thông báo thành công
            # 👉 Sau khi đăng ký xong thì chuyển sang trang dashboard
            return redirect("main_app:dashboard")
        else:
            # Nếu form không hợp lệ (ví dụ nhập sai dữ liệu)
            messages.error(request, "Có lỗi trong quá trình đăng ký.")
            return render(request, "signup.html", {"form": form})

    # Nếu request là GET (người dùng mới truy cập vào trang)
    # thì hiển thị form đăng ký trống
    return render(request, "signup.html", {"form": SignUpForm()})


# ---------------- Đăng nhập ----------------
def login_view(request):
    if request.method == "POST":   # Nếu user bấm nút đăng nhập
        form = LoginForm(request, data=request.POST)  # Lấy dữ liệu form
        if form.is_valid():        # Nếu form hợp lệ
            login(request, form.get_user())  # Đăng nhập bằng user đã xác thực
            # messages.success(request, "Đăng nhập thành công!")
            # 👉 Sau khi đăng nhập thành công thì chuyển sang dashboard
            return redirect("main_app:dashboard")
        else:
            # Nếu thông tin đăng nhập sai
            messages.error(request, "Sai email hoặc mật khẩu.")
            return render(request, "login.html", {"form": form})

    # Nếu request là GET → hiển thị form đăng nhập trống
    return render(request, "login.html", {"form": LoginForm()})


# ---------------- Đăng xuất ----------------
def logout_view(request):
    logout(request)   # Đăng xuất user hiện tại
    # messages.info(request, "Bạn đã đăng xuất.")  # Thông báo
    return redirect("home")  # Sau khi đăng xuất quay về trang chủ
