from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Table
from .forms import ReservationForm


def home(request: HttpRequest) -> HttpResponse:
    carousel_images = [
        'reservations/images/indoor.jpg',
        'reservations/images/bacalhau.jpg',
        'reservations/images/bitoque.jpg',
        'reservations/images/calamares.jpg',
        'reservations/images/francesinha.jpg',
        'reservations/images/hamburguer.jpg',
        'reservations/images/ovos-rotos.jpg',
        'reservations/images/pastel-de-nata.jpg',
    ]
    context = {"carousel_images": carousel_images}
    return render(request, "home.html", context)

# Create your views here.
def tables(request: HttpRequest) -> HttpResponse:
    available_tables = Table.objects.all()
    template = loader.get_template("tables.html")
    context = {"available_tables": available_tables}
    return HttpResponse(template.render(context, request))

# Views for the forms
def reservation(request: HttpRequest) -> HttpResponse:
    # If the user clicked to send the forms
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()                 # Creates and saves the reservation in the model
            return redirect("home")     # Redirects to home page after sending the forms
    # The user has just open the page
    else:
        form = ReservationForm()        # Shows empty forms
        
    return render(request, "reservation.html", {"form": form})