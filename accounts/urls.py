from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("", login_required(views.UserDetailView.as_view()), name="user_detail"),
]
