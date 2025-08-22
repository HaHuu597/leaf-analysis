# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # "/" sẽ vào home của accounts
    path('', include("main_app.urls", namespace="main_app")), # dashboard của app chính
]
