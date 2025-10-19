from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.html import format_html

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

# Views for the forms
def reservation(request: HttpRequest) -> HttpResponse:
    # If the user clicked to send the forms
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()                 # Creates and saves the reservation in the model
            messages.success(request, format_html("A tua reserva foi efetuada com <strong>sucesso</strong>!"))
            return redirect("home")     # Redirects to home page after sending the forms
    # The user has just open the page
    else:
        form = ReservationForm()        # Shows empty forms
    
    return render(request, "reservation.html", {"form": form})