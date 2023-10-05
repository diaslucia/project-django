from django.urls import path
from .views import home, courses, form, students, professors

urlpatterns = [
    path("", home, name="Home"),
    path("courses", courses, name="Courses"),
    path("form", form, name="Form"),
    path("students", students, name="Students"),
    path("professors", professors, name="Professors"),
]
