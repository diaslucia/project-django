from django.shortcuts import render
from .models import Course, Student, Professor
from .forms import CourseClass, SearchClass, StudentClass, ProfessorClass


def home(request):
    return render(request, "AppSchool/index.html")


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


def formStudent(request):
    if request.method == "POST":
        myForm = StudentClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data
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
        myForm = StudentClass()

    return render(request, "AppSchool/formStudent.html", {"myForm": myForm})


def formProfessor(request):
    if request.method == "POST":
        myForm = ProfessorClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data
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


def students(request):
    return render(
        request,
        "AppSchool/students.html",
        {"db": Student.objects.all()},
    )


def professors(request):
    return render(
        request,
        "AppSchool/professors.html",
        {"db": Professor.objects.all()},
    )
