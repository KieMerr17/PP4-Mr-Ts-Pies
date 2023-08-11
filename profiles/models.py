from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date

DIET = ((0, "No Special Requirement"), (1, "Vegetarian"), (2, "Pescetarian"), (3, "Vegan"), (4, "Nut Allergy"))


class UserProfile(models.Model):
    profile_picture = CloudinaryField('image', default='placeholder')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.BigIntegerField(default=123456789)
    dietary_requirements = models.IntegerField(choices=DIET, default=0)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.name