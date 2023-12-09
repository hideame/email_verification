from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

CustomUser = get_user_model()

message = """
Thank you for sign-up.
Please click the URL below to complete your sign-up.
"""


def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/accounts/signup/{}/{}/".format(uid, token)


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        # 確認するまでログイン不可にする
        user.is_active = False

        if commit:
            user.save()
            send_mail(
                "Sign-up confirmation",
                message + get_activate_url(user),
                getattr(settings, "EMAIL_HOST_USER", None),
                [user.email],
                fail_silently=False,
            )
        return user


def activate_user(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except Exception:
        return False

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True

    return False
