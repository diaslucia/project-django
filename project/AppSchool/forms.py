from django import forms


class CourseClass(forms.Form):
    name = forms.CharField(max_length=40)
    course = forms.IntegerField()


class SearchClass(forms.Form):
    name = forms.CharField(max_length=40)
