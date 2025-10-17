from django.contrib import admin
from django.utils import timezone

from .models import Reservation, Table

def daily_summary(modeladmin, request, queryset):
    reservations_today = queryset.filter(date__date=timezone.localdate())   # Filters for the reservations made today
    total_reservations = reservations_today.count()
    total_guests = sum(r.guests for r in reservations_today)            # Counts all the clients that were in the restaurant
    occupied_tables = len({r.table for r in reservations_today})     # Turns the object into a set and counts the number of tables
    available_tables = Table.objects.count() - occupied_tables
    
    message = {
        f"Total reservations: {total_reservations}, "
        f"Total guests: {total_guests}, "
        f"Occupied tables: {occupied_tables}, "
        f"Available tables: {available_tables}"
    }
    modeladmin.message_user(request, message)

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("table", "date", "first_name", "last_name", "guests", "phone_number", "notes")
    list_filter = ("table", "date",)
    actions = [daily_summary]

admin.site.register(Table)
admin.site.register(Reservation, ReservationAdmin)