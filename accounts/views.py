from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignUpForm, activate_user


class UserDetailView(TemplateView):
    template_name = "accounts/user_detail.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:signup_done")


class SignUpDoneView(TemplateView):
    template_name = "accounts/signup_done.html"


class SignUpCompleteView(TemplateView):
    template_name = "accounts/signup_complete.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)
