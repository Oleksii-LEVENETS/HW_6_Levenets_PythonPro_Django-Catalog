from math import pow, sqrt

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PersonForm, Triangle
from .models import Person


# Create your views here.
def index(request):
    return render(request, 'mess_app/index.html')


def triangle(request):
    form = Triangle(request.GET)

    if form.is_valid():
        leg_a = int(request.GET["leg_a"])
        leg_b = int(request.GET["leg_b"])
        hypotenuse = sqrt(pow(leg_a, 2) + pow(leg_b, 2))
        return render(request, 'mess_app/hypotenuse.html', {'hypotenuse': hypotenuse})

    else:
        form = Triangle(request.GET)

    return render(request, 'mess_app/hypotenuse.html', {'form': form, 'hypotenuse': None})


def create_person(request):
    pk = request.GET.get('id')
    if isinstance(pk, str) and len(pk) > 0:
        return redirect('mess_app:update-person', id=pk)

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("mess_app:create-person"))
    else:
        form = PersonForm(initial={"email": "example@dj.com"})
    return render(request, "mess_app/create_person.html", {"form": form})


def update_person(request, id):  # noqa: A002
    obj = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse("mess_app:index"))
    else:
        form = PersonForm(instance=obj)
    return render(request, "mess_app/update_person.html", {"form": form, "obj": obj})
