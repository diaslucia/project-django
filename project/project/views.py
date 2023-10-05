from django.http import HttpResponse
from django.template import Template, Context, loader

""" def get_detail(request, id):
    print(id)

def use_template(request):
    dictionary = {
        "name": "Lucia",
        "surname": "Dias",
        "cats": ["Booker", "Ciri"]
    }

    my_html = open('./templates/template1.html')
    template = Template(my_html.read())
    my_html.close()
    my_context= Context(dictionary)
    document = template.render(my_context)

    return HttpResponse(document)

def use_template2(request):
    dictionary = {
        "name": "Lucia",
        "surname": "Dias",
        "cats": ["Booker", "Ciri"]
    }

    my_context = loader.get_template("template1.html")
    document = my_context.render(dictionary)

    return HttpResponse(document)
 """