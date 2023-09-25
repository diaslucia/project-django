from datetime import datetime as dt
from django.http import HttpResponse
from django.template import Template, Context

def get_date(request):
    day = dt.now()
    return HttpResponse(f"Hoy es:{day}")

def get_detail(request, id):
    print(id)

def use_template(request):
    my_html = open('./templates/template1.html')
    template = Template(my_html.read())
    my_html.close()
    my_context= Context()
    document = template.render(my_context)

    return HttpResponse(document)
