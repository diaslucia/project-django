from django.shortcuts import render
from .models import Course, Student, Professor
from .forms import CourseClass, SearchClass

# Create your views here.


def home(request):
    return render(request, "AppSchool/index.html")


def form(request):
    if request.method == "POST":
        myForm = CourseClass(request.POST)

        if myForm.is_valid():
            info = myForm.cleaned_data
            courseInfo = Course(name=info["name"], course=info["course"])
            courseInfo.save()
            return render(request, "AppSchool/index.html")
    else:
        myForm = CourseClass()

    return render(request, "AppSchool/form.html", {"myForm": myForm})


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
