# from django.urls import path
# from . import views

# app_name = 'main_app'

# urlpatterns = [
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path("upload/", views.upload_and_predict, name="upload"),
#     path("history/", views.history, name="history"),
# ]



from django.urls import path
from . import views

app_name = "main_app"   # ✅ bắt buộc phải có nếu muốn dùng namespace

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
