from django.contrib import admin
from .models import Course, Student, Professor, Avatar

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Avatar)
