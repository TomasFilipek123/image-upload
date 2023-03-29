from django.contrib import admin
from .models import Image, UserProfile, Tier, Size
# Register your models here.
admin.site.register(Image)
admin.site.register(UserProfile)
admin.site.register(Tier)
admin.site.register(Size)
