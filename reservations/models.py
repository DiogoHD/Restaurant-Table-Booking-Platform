from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta

RESERVATION_DURATION = timedelta(hours=2)

# Create your models here.
class Table(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    seats = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    date = models.DateTimeField()
    guests = models.PositiveSmallIntegerField()
    # Foreign Key allows for multiple reservations in the same table
    # on_delete=models.CASCADE means that if the table is deleted, all reservations in that table are deleted too
    table = models.ForeignKey(Table, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} - Table {self.table.number} at {self.date}"
    
    def is_available(self, table: Table) -> bool:
        # Filters all the objects for the table
        start_time = self.date
        end_time = self.date + RESERVATION_DURATION
        
        # Loops through all reservations in that table
        # exclude(pk=self.pk) ignores self object whn editing the data base
        for r in Reservation.objects.filter(table=table).exclude(pk=self.pk):     
            r_start = r.date
            r_end = r.date + RESERVATION_DURATION
            
            # If the new reservation starts before the existing reservation ends and the new reservation ends after the new reservation starts
            if (start_time < r_end) and (end_time > r_start):
                return False
        
        return True
    
    # Clean allows form validation
    def clean(self):
        # Checks if the table has enough seats for the guests
        if self.table and self.guests > self.table.seats:
            raise ValidationError(f"The table {self.table.number} only has {self.table.seats} seats and you have {self.guests} guests.")
        
        # Checks if the phone number is a valid portuguese number
        phone = str(self.phone_number)
        if len(phone) != 9 or phone[0] != '9':
            raise ValidationError(f"Your phone number must have 9 digits and start with a 9.")
        
        # Checks if the table is available at that time (each reservation has a standard duration of 2 hours)
        if self.table:
            if not self.is_available(self.table):
                raise ValidationError(f"The table {self.table.number} is already booked for this time.")
        
        # If the user doesn't choose a table, a table is automatically assigned
        else:
            for t in Table.objects.all():
                if self.guests <= t.seats and self.is_available(t):
                    self.table = t
                    break
            
            if not self.table:
                raise ValidationError(f"Sorry, the restaurant is fully booked at this time.")