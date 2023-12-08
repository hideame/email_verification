from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

TopView = TemplateView.as_view(template_name="top.html")

urlpatterns = [
    path("", TopView, name="top"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("registration/", include("django.contrib.auth.urls")),
]
