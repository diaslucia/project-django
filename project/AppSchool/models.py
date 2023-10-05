from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    course = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Professor(models.Model):
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
