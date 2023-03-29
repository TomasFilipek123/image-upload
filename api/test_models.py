from django.db import models
from PIL import Image as Img
from django.contrib.auth.models import User


class Image(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    thumbnail_200 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    expiration_time = models.IntegerField(null=True, blank=True)

    BASIC = 'B'
    PREMIUM = 'P'
    ENTERPRISE = 'E'
    PLAN_CHOICES = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]
    plan = models.CharField(max_length=1, choices=PLAN_CHOICES, default=BASIC)

    def __str__(self):
        return self.image.name

