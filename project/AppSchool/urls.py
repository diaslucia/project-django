from django.urls import path
from .views import (
    home,
    courses,
    formCourse,
    formStudent,
    formProfessor,
    students,
    professors,
)

urlpatterns = [
    path("", home, name="Home"),
    path("courses", courses, name="Courses"),
    path("formCourse", formCourse, name="FormCourse"),
    path("formStudent", formStudent, name="FormStudent"),
    path("formProfessor", formProfessor, name="FormProfessor"),
    path("students", students, name="Students"),
    path("professors", professors, name="Professors"),
]
