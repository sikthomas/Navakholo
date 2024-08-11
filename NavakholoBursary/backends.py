from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class IdNumberBackend(ModelBackend):
    def authenticate(self, request, idnumber=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(idnumber=idnumber)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
