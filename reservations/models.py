from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Table(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    seats = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    date = models.DateTimeField()
    guests = models.PositiveSmallIntegerField()
    # Foreign Key allows for multiple reservations in the same table
    # on_delete=models.CASCADE means that if the table is deleted, all reservations in that table are deleted too
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Table {self.table.number} at {self.date}"
    
    # Clean allows form validation
    def clean(self):
        if self.table and self.guests > self.table.seats:
            raise ValidationError(f"The table {self.table.number} only has {self.table.seats} seats and you have {self.guests} guests.")
        
        if len(str(self.phone_number)) != 9:
            raise ValidationError(f"Your phone number must have 9 digits")