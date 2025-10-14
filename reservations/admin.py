from django.contrib import admin

from .models import Reservation, Table


# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ("table", "date", "first_name", "last_name", "guests", "phone_number", "notes")

admin.site.register(Table)
admin.site.register(Reservation, TableAdmin)