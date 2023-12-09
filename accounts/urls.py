from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", login_required(views.UserDetailView.as_view()), name="user_detail"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup/done/", views.SignUpDoneView.as_view(), name="signup_done"),
    path("signup/<uidb64>/<token>/", views.SignUpCompleteView.as_view(), name="signup_complete"),
]
