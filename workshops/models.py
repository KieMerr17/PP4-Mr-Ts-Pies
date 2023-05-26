from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
BOOKING = ((0, "Pending"), (1, "Approved"))

class Workshop(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workshop_event")
    event_date = models.DateField()
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
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.name}: {self.body}"


class Make_Booking(models.Model):
    post = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name="reserve_space")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    booked_on = models.DateTimeField(auto_now_add=True)
    request_space = models.IntegerField(choices=BOOKING, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return self.title



# Create your models here.
