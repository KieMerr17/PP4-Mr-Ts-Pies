from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Pie, Allergy

# These tests first create a Pie, then tests it loads on the assigned template,
# it can be liked/unliked by the user, and checks for 404 error


class PieTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.allergy_milk = Allergy.objects.create(allergy=0)
        self.pie = Pie.objects.create(
            title='Test Pie',
            slug='test-pie',
            description='This is a test pie.',
            diet=0,
        )
        self.client.login(username='testuser', password='testpassword')

    # Test Pies load on the pies.html template
    def test_pie_list_view(self):
        response = self.client.get(reverse('pies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pies.html')
        self.assertContains(response, 'Test Pie')

    # Test function to like a Pie and its link to the user
    def test_pie_like_view(self):
        response = self.client.post(reverse('pie_like', args=[self.pie.slug]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.pie.refresh_from_db()
        self.assertTrue(self.pie.likes.filter(id=self.user.id).exists())

    # Test function to unlike a Pie and its un-link to the user
    def test_pie_unlike_view(self):
        self.pie.likes.add(self.user)
        response = self.client.post(reverse('pie_like', args=[self.pie.slug]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.pie.refresh_from_db()
        self.assertFalse(self.pie.likes.filter(id=self.user.id).exists())

    # Test 404 page loads for non existent Pie
    def test_pie_like_view_nonexistent_pie(self):
        response = self.client.post(
            reverse('pie_like', args=['nonexistent-pie']))
        self.assertEqual(response.status_code, 404)
