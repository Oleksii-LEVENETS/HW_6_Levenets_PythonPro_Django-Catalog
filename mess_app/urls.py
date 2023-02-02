from django.urls import path

from . import views

app_name = "mess_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.create_person, name='create-person'),
    path('person/<int:id>/', views.update_person, name='update-person'),
]
