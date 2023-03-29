from django.db import models
from PIL import Image as Img
from django.contrib.auth.models import AbstractUser

class Size(models.Model):
    name = models.CharField(max_length=50, blank=True)
    width = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Tier(models.Model):
    name = models.CharField(max_length=50)
    original_image_link = models.BooleanField(default=False)
    expiring_links = models.BooleanField(default=False)
    size = models.ManyToManyField(Size)

    def __str__(self):
        return self.name
# Jak zrobić, żeby unrestricted było logicznie powiązane z UNRESTRICTED, tak żeby
# po wybracniu tej opcji pojawiawiała się możliwość wyboru planu
class UserProfile(AbstractUser):
    """Arbitrary plan should be in tiers so """
    email = models.CharField(max_length=80, unique=True, default=None)
    user_tier = models.OneToOneField(Tier, on_delete=models.CASCADE, default=None, null=True)
    username = models.CharField(max_length=46)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Image(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    original_link = models.URLField(null=True, blank=True)

    def __str__(self):
      return self.image.name



class Thumbnail(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumnbails/')
    original_link = models.URLField(null=True, blank=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)

    

