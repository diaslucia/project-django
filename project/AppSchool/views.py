from django.shortcuts import render
from .models import Course, Student, Professor
from .forms import CourseClass, SearchClass, StudentClass, ProfessorClass, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, "AppSchool/index.html")


@login_required
@staff_member_required
def formCourse(request):
    if request.method == "POST":
        myForm = CourseClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data
            courseInfo = Course(name=info["name"], course=info["course"])
            courseInfo.save()
            return render(
                request,
                "AppSchool/courses.html",
                {"myForm": myForm, "db": Course.objects.all()},
            )
    else:
        myForm = CourseClass()

    return render(request, "AppSchool/formCourse.html", {"myForm": myForm})


@login_required
@staff_member_required
def formStudent(request, id=None):
    if request.method == "POST":
        myForm = StudentClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data

            if id:
                getStudent = Student.objects.get(id=id)
                getStudent.name = info["name"]
                getStudent.lastName = info["lastName"]
                getStudent.email = info["email"]
                getStudent.save()
            else:
                courseInfo = Student(
                    name=info["name"], lastName=info["lastName"], email=info["email"]
                )
                courseInfo.save()

            return render(
                request,
                "AppSchool/students.html",
                {"db": Student.objects.all()},
            )
    else:
        if id:
            getStudent = Student.objects.get(id=id)
            myForm = StudentClass(
                initial={
                    "name": getStudent.name,
                    "lastName": getStudent.lastName,
                    "email": getStudent.email,
                }
            )
        else:
            myForm = StudentClass()

    return render(request, "AppSchool/formStudent.html", {"myForm": myForm})


@staff_member_required
def formProfessor(request, id=None):
    if request.method == "POST":
        myForm = ProfessorClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data

            if id:
                getProfessor = Professor.objects.get(id=id)
                getProfessor.name = info["name"]
                getProfessor.lastName = info["lastName"]
                getProfessor.email = info["email"]
                getProfessor.save()
            else:
                courseInfo = Professor(
                    name=info["name"], lastName=info["lastName"], email=info["email"]
                )
                courseInfo.save()

            return render(
                request,
                "AppSchool/professors.html",
                {"db": Professor.objects.all()},
            )
    else:
        if id:
            getProfessor = Professor.objects.get(id=id)
            myForm = ProfessorClass(
                initial={
                    "name": getProfessor.name,
                    "lastName": getProfessor.lastName,
                    "email": getProfessor.email,
                }
            )
        else:
            myForm = ProfessorClass()

    return render(request, "AppSchool/formProfessor.html", {"myForm": myForm})


def courses(request):
    if request.method == "POST":
        myForm = SearchClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data
            db = Course.objects.filter(name__icontains=info["name"])
            return render(
                request, "AppSchool/courses.html", {"myForm": myForm, "db": db}
            )
    else:
        myForm = SearchClass()

    return render(
        request,
        "AppSchool/courses.html",
        {"myForm": myForm, "db": Course.objects.all()},
    )


def students(request, id=None):
    if id:
        findItem = Student.objects.get(id=int(id))
        findItem.delete()

    return render(
        request,
        "AppSchool/students.html",
        {"db": Student.objects.all()},
    )


def professors(request, id=None):
    if id:
        findItem = Professor.objects.get(id=int(id))
        findItem.delete()

    return render(
        request,
        "AppSchool/professors.html",
        {"db": Professor.objects.all()},
    )


""" User """


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            user_name = authenticate(username=user, password=passw)

            if user is not None:
                login(request, user_name)
                return render(request, "AppSchool/index.html")
            else:
                form = AuthenticationForm()
                return render(
                    request,
                    "AppSchool/login.html",
                    {"message": "Credencials incorrect", "form": form},
                )
        else:
            return render(request, "AppSchool/index.html")
    form = AuthenticationForm()
    return render(
        request,
        "AppSchool/login.html",
        {"form": form},
    )


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data["username"]
            form.save()
            return render(
                request,
                "AppSchool/index.html",
                {"message": "User added"},
            )

    else:
        form = UserRegisterForm()

    return render(
        request,
        "AppSchool/signup.html",
        {"form": form},
    )


@staff_member_required
def editProfile(request):
    user = request.user

    if request.method == "POST":
        myForm = UserEditForm(request.POST, request.FILES)

        if myForm.is_valid():
            formData = myForm.cleaned_data

            if formData["password1"] != formData["password2"]:
                datos = {"first_name": user.first_name, "email": user.email}
                myForm = UserEditForm(initial=datos)

            else:
                user.email = formData["email"]
                if formData["password1"]:
                    user.set_password(formData["password1"])
                user.last_name = formData["last_name"]
                user.first_name = formData["first_name"]
                user.save()

                # New avatar for user
                try:
                    avatarUser = Avatar.objects.get(user=user)
                except Avatar.DoesNotExist:
                    avatarUser = Avatar(user=user, avatar=formData["avatar"])
                    avatarUser.save()
                else:
                    avatarUser.avatar = formData["avatar"]
                    avatarUser.save()

                return render(request, "AppSchool/index.html")

    else:
        data = {"first_name": user.first_name, "email": user.email}
        myForm = UserEditForm(initial=data)

    return render(
        request, "AppSchool/editProfile.html", {"myForm": myForm, "user": user}
    )
