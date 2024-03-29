from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

ALLERGIES = ((0, "Milk"), (1, "Egg"), (2, "Fish"), (3, "Nuts"), (4, "Soy"))
DIET = ((0, "Meat"), (1, "Vegetarian"), (2, "Pescetarian"), (3, "Vegan"),
        (4, "Nut Allergy"))


# Reference the ALLERGIES, for use in selection
class Allergy(models.Model):
    allergy = models.IntegerField(choices=ALLERGIES, default=0)

    def __str__(self):
        return ALLERGIES[self.allergy][1]


# Database fields for Pie model
class Pie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    diet = models.IntegerField(choices=DIET, default=0)
    allergies = models.ManyToManyField(Allergy, blank=True)
    likes = models.ManyToManyField(User, related_name='pie_likes', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
