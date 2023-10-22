from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CourseClass(forms.Form):
    name = forms.CharField(max_length=40)
    course = forms.IntegerField()


class StudentClass(forms.Form):
    name = forms.CharField(max_length=40)
    lastName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)


class ProfessorClass(forms.Form):
    name = forms.CharField(max_length=40)
    lastName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)


class SearchClass(forms.Form):
    name = forms.CharField(max_length=40)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repeat your password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Repeat your password", widget=forms.PasswordInput, required=False
    )

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name", "password1", "password2"]
