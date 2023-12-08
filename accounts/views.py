# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignUpForm


class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    # success_url = reverse_lazy("accounts:signup")  # login画面実装するまでの暫定
    success_url = reverse_lazy("login")


class UserDetailView(TemplateView):
    template_name = "accounts/user_detail.html"
