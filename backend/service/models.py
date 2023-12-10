from __future__ import annotations

from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.conf import settings

from server.tools import RandomString, Choices


__all__ = [
    "Role",
    "Staff",
]


class Role(Choices):
    admin = "GodMode administrator"
    staff = "Standard staff member"
    moderator = "Reduced rights moderator"
    inactive = "Inactive account"


class StaffManager(BaseUserManager):
    def create_superuser(self, **kwargs) -> Staff:
        user = self.model(
            login=kwargs["login"],
            password=kwargs["password"],
            role=self.model.Roles.admin.name,
        )
        user.save()
        return user


class JunkDjangoUserMixin:
    is_admin: bool

    is_staff = True
    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["password"]

    def has_module_permission(self, request):
        return self.is_admin

    def has_module_perms(self, request):
        return self.is_admin

    def has_perm(self, request):
        return self.is_admin


class Staff(AbstractBaseUser, JunkDjangoUserMixin):
    Roles = Role

    login = models.CharField(
        verbose_name="Staff account name",
        max_length=48,
        unique=True,
    )
    password = models.CharField(
        verbose_name="Password",
        max_length=146,
    )
    pepper = RandomString(
        verbose_name="Pepper for hashing",
        max_length=16,
    )
    role = models.CharField(
        verbose_name="Staff role",
        choices=tuple((r.name, r.value) for r in Roles),
        max_length=12,
        default=Roles.inactive.name,
    )

    objects = StaffManager()

    @property
    def is_admin(self) -> bool:
        return self.role == self.Roles.admin.name

    @property
    def is_inactive(self) -> bool:
        return self.role == self.Roles.inactive.name

    def hash_raw_password(self, password: str) -> str:
        return make_password(password, settings.SALT + str(self.pepper))

    def set_password(self, raw_password):
        self.password = self.hash_raw_password(raw_password)
        self._password = raw_password

    def check_password(self, password) -> bool:
        pass_hash = self.hash_raw_password(password)
        return self.password == pass_hash

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff members"
        indexes = [
            models.Index(fields=["login"], name="staff_idx_login"),
            models.Index(fields=["role"], name="staff_idx_role"),
        ]

    def __str__(self):
        return str(self.login)

    def __str_admin__(self) -> str:
        return f"{self.login} / {self.role}"
