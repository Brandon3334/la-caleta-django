from django.urls import path

from . import views

app_name = "carta"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("plato/<int:id>/", views.detalle, name="detalle"),
]
