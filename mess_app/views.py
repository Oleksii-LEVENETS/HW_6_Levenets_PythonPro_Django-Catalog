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
        gipo = ((leg_a ** 2) + (leg_b ** 2)) ** 0.5
        return render(request, 'mess_app/base.html', {'gipo': gipo})

    else:
        form = Triangle()

    return render(request, 'mess_app/base.html', {'form': form, 'gipo': None})
