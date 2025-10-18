from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reservation/", views.reservation, name="reservation"),
    path("tables/", views.tables, name="tables"),
]