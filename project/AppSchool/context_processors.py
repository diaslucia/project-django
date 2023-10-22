# context_processors.py
from django.contrib.auth.context_processors import auth
from .models import Avatar


def custom_user(request):
    context = auth(request)
    user = context["user"]

    if user.is_authenticated:
        image = Avatar.objects.filter(user=request.user.id)
        imageQty = len(image)
        if imageQty > 0:
            context["avatarUser"] = image[imageQty - 1]
        else:
            context["avatarUser"] = ""

    return context
