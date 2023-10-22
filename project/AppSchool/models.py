from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=40)
    course = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.course}"


class Student(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.lastName}"


class Professor(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.lastName}"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.avatar}"
