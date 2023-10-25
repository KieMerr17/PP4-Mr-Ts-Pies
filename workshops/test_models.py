from django.test import TestCase
from .models import Workshop, Booking
from django.contrib.auth.models import User
from datetime import date


# This test Checks the the workshop created is created, the tite and user
# are correctly imported, the likes and future event function

class WorkshopModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                    username='testuser', password='testpassword')
        self.workshop = Workshop.objects.create(
            title='Test Workshop',
            slug='test-workshop',
            event_date=date(2023, 11, 1),
            spaces=10,
            chef=self.user,
            content='Test content'
        )

    def test_workshop_title(self):
        self.assertEqual(self.workshop.title, 'Test Workshop')

    def test_chef_user_relation(self):
        self.assertEqual(self.workshop.chef, self.user)

    def test_number_of_likes(self):
        self.assertEqual(self.workshop.number_of_likes(), 0)

    def test_future_event(self):
        self.assertTrue(self.workshop.future_event())


# This tests that bookings made are valid and are assigned to the workshop

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                    username='testuser', password='testpassword')
        self.workshop = Workshop.objects.create(
            title='Test Workshop',
            slug='test-workshop',
            event_date=date(2023, 11, 1),
            spaces=10,
            chef=self.user,
            content='Test content'
        )
        self.booking = Booking.objects.create(
            user=self.user,
            workshop=self.workshop,
            name='Test User',
            email='test@example.com',
            phone_number='123456789',
            spaces=2,
            dietary_requirements=1
        )

    def test_clean_method(self):
        # Test the booking is valid
        self.booking.clean()
        self.workshop.refresh_from_db()
        self.assertEqual(self.workshop.spaces, 10)

    def test_save_method(self):
        # Test the booking is saved
        self.booking.save()
        self.workshop.refresh_from_db()
        self.assertEqual(self.workshop.spaces, 10)
