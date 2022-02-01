from django.db import models

from users.models import AuthUser


class Location(models.Model):

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.city} - {self.country}"


class Logs(models.Model):

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
