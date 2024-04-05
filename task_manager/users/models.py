from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.hashers import make_password
#
#
# # Create your models here.
# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

from django.contrib.auth.models import User


class CustomUser(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()
