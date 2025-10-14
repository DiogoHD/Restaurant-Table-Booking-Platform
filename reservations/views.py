from django.http import HttpResponse
from django.template import loader

from .models import Table


# Create your views here.
def tables(request):
    available_tables = Table.objects.all()
    template = loader.get_template("main.html")
    context = {"available_tables": available_tables}
    return HttpResponse(template.render(context, request))