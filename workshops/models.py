from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from django.contrib.auth import get_user_model

STATUS = ((0, "Draft"), (1, "Published"))


# Database fields for Workshop model
class Workshop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_date = models.DateField()
    spaces = models.IntegerField(default=6)
    chef = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_chef"
        )
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='workshop_likes', blank=True
        )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def future_event(self):
        return self.event_date > date.today()


DIET = (
    (0, "No Special Requirement"),
    (1, "Vegetarian"),
    (2, "Pescetarian"),
    (3, "Vegan"),
    (4, "Nut Allergy")
)


# Database fields for Booking model
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name="bookings"
        )
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, related_name="bookings"
        )
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
        if self.spaces <= 0:
            raise ValidationError(
                "Please cancel your booking if you do not require any spaces"
                )

        if self.approved:
            # Check if it's a new booking (no primary key) or an existing one
            if self.pk is None:
                new_spaces = self.workshop.spaces - self.spaces
                if new_spaces < 0:
                    raise ValidationError(
                        "Requested spaces exceed available spaces"
                        )
                else:
                    self.workshop.spaces = new_spaces
                    # Save the related workshop with updated spaces
                    self.workshop.save()
            else:
                original_booking = Booking.objects.get(pk=self.pk)
                original_approved = original_booking.approved
                new_approved = self.approved
                if original_approved:
                    if original_booking.spaces != self.spaces:
                        space_diff = self.spaces - original_booking.spaces
                        new_spaces = self.workshop.spaces - space_diff
                        if new_spaces < 0:
                            raise ValidationError(
                                "Requested spaces exceed available spaces"
                                )
                        else:
                            self.workshop.spaces = new_spaces
                            # Save the related workshop with updated spaces
                            self.workshop.save()
                elif new_approved:
                    check_spaces = self.workshop.spaces - self.spaces
                    if check_spaces < 0:
                        raise ValidationError(
                            "Requested spaces exceed available spaces"
                            )
                    else:
                        self.workshop.spaces = check_spaces
                        # Save the related workshop with updated spaces
                        self.workshop.save()

        else:  # Booking changed from approved to unapproved
            if self.pk is None:
                self.workshop.save()
            else:
                original_booking = Booking.objects.get(pk=self.pk)
                original_approved = original_booking.approved
                new_spaces = self.workshop.spaces + self.spaces
                if not original_booking.approved:
                    self.workshop.save()
                else:
                    self.workshop.spaces = new_spaces
                    # Save the related workshop with updated spaces
                    self.workshop.save()

    def save(self, *args, **kwargs):
        self.workshop.save()  # Save the related workshop with updated spaces
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.approved:
            # Return spaces to the workshop when an approved booking is deleted
            self.workshop.spaces += self.spaces
        self.workshop.save()
        super().delete(*args, **kwargs)
