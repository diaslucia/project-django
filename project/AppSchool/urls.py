from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    home,
    courses,
    formCourse,
    formStudent,
    formProfessor,
    students,
    professors,
    login_req,
    signup,
    editProfile,
)

urlpatterns = [
    path("", home, name="Home"),
    path("courses", courses, name="Courses"),
    path("students", students, name="Students"),
    path("students/<int:id>", students, name="Students"),
    path("professors", professors, name="Professors"),
    path("professors/<int:id>", professors, name="Professors"),
]

urlpatterns += [
    path("formCourse", formCourse, name="FormCourse"),
    path("formStudent", formStudent, name="FormStudent"),
    path("formStudent/<int:id>", formStudent, name="FormStudent"),
    path("formProfessor", formProfessor, name="FormProfessor"),
    path("formProfessor/<int:id>", formProfessor, name="FormProfessor"),
]

urlpatterns += [
    path("login", login_req, name="Login"),
    path("signup", signup, name="Signup"),
    path(
        "logout",
        LogoutView.as_view(template_name="AppSchool/index.html"),
        name="Logout",
    ),
    path("editProfile", editProfile, name="EditProfile"),
]
