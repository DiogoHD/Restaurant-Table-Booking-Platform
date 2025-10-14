from django.urls import path

from . import views

urlpatterns = [
    path('reservations/', views.tables, name='tables'),
]