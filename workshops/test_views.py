from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Workshop, Booking


# This test creates a workshop, tests it can be viewed.
# It also tests booking creation, editing and deleting views.

class WorkshopViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                    username='testuser', password='testpassword')
        self.workshop = Workshop.objects.create(
            title='Test Workshop',
            slug='test-workshop',
            event_date='2023-12-31',
            spaces=10,
            chef=self.user,
            content='Test content',
        )

    def test_workshop_list_view(self):
        response = self.client.get(reverse('workshops'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.workshop in response.context['workshop_list'])

    def test_book_workshop_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
                    reverse('book_workshop', args=[self.workshop.id]))
        self.assertEqual(response.status_code, 200)

    # preload the view with the booking details
    def test_edit_booking_view(self):
        booking = Booking.objects.create(
            user=self.user,
            workshop=self.workshop,
            name='Test User',
            email='test@example.com',
            phone_number=123456789,
            spaces=2,
            dietary_requirements=0,
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 200)

    # create a booking to test the delete booking view
    def test_delete_booking_view(self):
        booking = Booking.objects.create(
            user=self.user,
            workshop=self.workshop,
            name='Test User',
            email='test@example.com',
            phone_number=123456789,
            spaces=2,
            dietary_requirements=0,
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
                    reverse('delete_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
