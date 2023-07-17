from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

STATUS = ((0, "Draft"), (1, "Published"))


class Workshop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_date = models.DateField()
    spaces = models.IntegerField(default=6)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_chef")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='workshop_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.name}: {self.body}"


DIET = ((0, "No Special Requirement"), (1, "Vegetarian"), (2, "Pescetarian"), (3, "Vegan"), (4, "Nut Allergy"))


class Booking(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name="workshop")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.BigIntegerField(default=123456789)
    spaces = models.IntegerField(default=1)
    dietary_requirements = models.IntegerField(choices=DIET, default=0)
    booked_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return f"Booking for {self.name} - Workshop: {self.workshop}"

    def clean(self):
        if self.spaces > self.workshop.spaces:
            raise ValidationError("The number of spaces booked exceeds the available spaces in the workshop.")

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.approved:
                # Only reduce the number of spaces when a new booking is created
                self.workshop.spaces -= self.spaces
        else:
            original_booking = Booking.objects.get(pk=self.pk)
            if original_booking.approved and not self.approved:
                # Increase the number of spaces when an approved booking is modified to be unapproved
                self.workshop.spaces += original_booking.spaces
            elif not original_booking.approved and self.approved:
                # Reduce the number of spaces when an unapproved booking is modified to be approved
                self.workshop.spaces -= self.spaces
        
        self.workshop.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Add the spaces back to the workshop when a booking is deleted
        self.workshop.spaces += self.spaces
        self.workshop.save()
        super().delete(*args, **kwargs)