from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # メールアドレスとパスワードで認証
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        # メールアドレスとパスワードで認証
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # 以下をオーバーライド
    username = models.CharField(_("username"), max_length=150)  # emailを一意にするので、usernameはuniqueの制限を外す
    email = models.EmailField(unique=True)  # 認証で使うので入力必須かつユニークに
    USERNAME_FIELD = "email"  # USERNAMEフィールドをusernameからemailに
    REQUIRED_FIELDS = []  # emailがデフォルトで入っていてエラーになるので除外する
    objects = CustomUserManager()  # UserManagerクラスの代わりに今回作成するCustomUserManagerクラスを呼び出す
