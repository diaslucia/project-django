from django import forms


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
