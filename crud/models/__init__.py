from django.db import models
from django.contrib import admin


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


admin.site.register(User)
