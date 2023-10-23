from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Professor


class About(TemplateView):
    template_name = "AppCoder/about.html"


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = "AppCoder/professorDetail.html"
