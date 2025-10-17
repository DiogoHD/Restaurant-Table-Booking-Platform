from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Table


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {})

# Create your views here.
def tables(request: HttpRequest) -> HttpResponse:
    available_tables = Table.objects.all()
    template = loader.get_template("tables.html")
    context = {"available_tables": available_tables}
    return HttpResponse(template.render(context, request))