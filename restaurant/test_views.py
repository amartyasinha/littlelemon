from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from .models import Menu, Booking
from datetime import date, time


class MenuViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(
            title="Pizza",
            price=Decimal('15.00'),
            inventory=5,
            description="Delicious pizza"
        )

    def test_get_menu_list(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        data = {
            'title': 'Burger',
            'price': '10.00',
            'inventory': 8,
            'description': 'Tasty burger'
        }
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)

    def test_get_menu_item_detail(self):
        response = self.client.get(f'/api/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pizza')


class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking = Booking.objects.create(
            name="Jane Smith",
            number_of_guests=2,
            booking_date=date(2024, 2, 20),
            booking_time=time(18, 0)
        )

    def test_get_booking_list(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        data = {
            'name': 'Bob Wilson',
            'number_of_guests': 3,
            'booking_date': '2024-03-15',
            'booking_time': '20:00'
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_get_booking_detail(self):
        response = self.client.get(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Smith')


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Little Lemon Restaurant')