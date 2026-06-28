from django.test import TestCase
from decimal import Decimal
from .models import Menu, Booking
from datetime import date, time


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pasta",
            price=Decimal('12.50'),
            inventory=10,
            description="Delicious pasta dish"
        )

    def test_menu_creation(self):
        self.assertEqual(self.menu_item.title, "Pasta")
        self.assertEqual(self.menu_item.price, Decimal('12.50'))
        self.assertEqual(self.menu_item.inventory, 10)
        self.assertEqual(self.menu_item.description, "Delicious pasta dish")

    def test_menu_str_method(self):
        expected_str = "Pasta - $12.50"
        self.assertEqual(str(self.menu_item), expected_str)


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date=date(2024, 1, 15),
            booking_time=time(19, 30)
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.number_of_guests, 4)
        self.assertEqual(self.booking.booking_date, date(2024, 1, 15))
        self.assertEqual(self.booking.booking_time, time(19, 30))

    def test_booking_str_method(self):
        expected_str = "John Doe - 2024-01-15 at 19:30"
        self.assertEqual(str(self.booking), expected_str)