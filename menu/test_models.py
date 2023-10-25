from django.test import TestCase
from .models import Allergy, Pie
from django.contrib.auth.models import User


# These tests will create a Pie item, check the max length of title,
# a description can be added and a pie gives total likes count.
# Also check that a DIET and ALLERGY can be associated to the pie.

class PieModelTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
                        username='testuser', password='testpassword')
        allergy = Allergy.objects.create(allergy=0)

        self.pie = Pie.objects.create(
            title='Test Pie',
            slug='test-pie',
            description='Test description',
            featured_image='placeholder',
            excerpt='Test excerpt',
            diet=0
        )
        self.pie.allergies.add(allergy)
        self.pie.likes.add(test_user)

    def test_title_max_length(self):
        max_length = self.pie._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_description(self):
        self.assertEqual(self.pie.description, 'Test description')

    def test_likes_count(self):
        self.assertEqual(self.pie.likes.count(), 1)

    def test_diet_default_value(self):
        self.assertEqual(self.pie.diet, 0)

    def test_allergies_count(self):
        self.assertEqual(self.pie.allergies.count(), 1)


# This tests to confirm that new ALLERGY objects can be created
class AllergyModelTest(TestCase):

    def test_allergy_str_method(self):
        allergy = Allergy.objects.create(allergy=1)
        self.assertEqual(str(allergy), 'Egg')
