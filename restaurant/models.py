from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - ${self.price}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date} at {self.booking_time:%H:%M}"
