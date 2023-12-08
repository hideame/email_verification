from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView

TopView = TemplateView.as_view(template_name="top.html")
UserDetailView = TemplateView.as_view(template_name="registration/user_detail.html")

urlpatterns = [
    path("", TopView, name="top"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("registration/", login_required(UserDetailView), name="user_detail"),
    path("registration/", include("django.contrib.auth.urls")),
]
