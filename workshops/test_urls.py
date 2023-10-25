from django.test import TestCase
from django.urls import reverse, resolve
from .views import WorkshopList, WorkshopDetail, book_workshop, edit_booking, delete_booking



# These tests check that the Workshop and booking urls
# work correctly 

class TestUrls(TestCase):
    def test_workshop_list_url_resolves(self):
        url = reverse('workshops')
        self.assertEqual(resolve(url).func.view_class, WorkshopList)

    def test_workshop_detail_url_resolves(self):
        url = reverse('workshop_detail', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, WorkshopDetail)

    def test_book_workshop_url_resolves(self):
        url = reverse('book_workshop', args=[1])
        self.assertEqual(resolve(url).func, book_workshop)

    def test_edit_booking_url_resolves(self):
        url = reverse('edit_booking', args=[1])
        self.assertEqual(resolve(url).func, edit_booking)

    def test_delete_booking_url_resolves(self):
        url = reverse('delete_booking', args=[1])
        self.assertEqual(resolve(url).func, delete_booking)
