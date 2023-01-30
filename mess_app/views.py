from math import pow, sqrt

from django.http import HttpResponse
from django.shortcuts import render

from .forms import Triangle


# Create your views here.
def index(request):
    return HttpResponse("Hello, you're at the 'mess_app' index.")


def triangle(request):
    form = Triangle(request.GET)

    if form.is_valid():
        leg_a = int(request.GET["leg_a"])
        leg_b = int(request.GET["leg_b"])
        hypotenuse = sqrt(pow(leg_a, 2) + pow(leg_b, 2))
        return render(request, 'mess_app/base.html', {'hypotenuse': hypotenuse})

    else:
        form = Triangle(request.GET)

    return render(request, 'mess_app/base.html', {'form': form, 'hypotenuse': None})
