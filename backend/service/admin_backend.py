from django.contrib.auth.backends import ModelBackend

from .models import Staff


class AdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get("login")
        if username is None or password is None:
            return

        try:
            user = Staff.objects.get(login=username)
        except Staff.DoesNotExist:
            user = Staff()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

    def user_can_authenticate(self, user: Staff) -> bool:
        return not user.is_inactive
