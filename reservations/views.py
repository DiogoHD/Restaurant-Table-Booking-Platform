from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Table

def home(request):
    return render(request, "home.html", {})

# Create your views here.
def tables(request):
    available_tables = Table.objects.all()
    template = loader.get_template("tables.html")
    context = {"available_tables": available_tables}
    return HttpResponse(template.render(context, request))