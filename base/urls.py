from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("", csrf_exempt(views.index), name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
]
