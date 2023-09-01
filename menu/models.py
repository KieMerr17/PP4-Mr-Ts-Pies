from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

ALLERGIES = ((0, "Milk"), (1, "Egg"), (2, "Fish"), (3, "Nuts"), (4, "Soy"))
DIET = ((0, "Meat"), (1, "Vegetarian"), (2, "Pescetarian"), (3, "Vegan"), (4, "Nut Allergy"))


class Allergy(models.Model):
    allergy = models.IntegerField(choices=ALLERGIES, default=0)

    def __str__(self):
        return ALLERGIES[self.allergy][1]


class Pie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    diet = models.IntegerField(choices=DIET, default=0)
    allergies = models.ManyToManyField(Allergy, blank=True)

    def __str__(self):
        return self.title