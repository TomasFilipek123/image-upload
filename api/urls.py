from django.urls import path
from .views import ImageList, generate_expiring_link, ImageViewSet
from rest_framework.authtoken import views
from django.conf.urls.static import static  #new
from django.conf import settings     #new

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/link/', generate_expiring_link, name='generate-expiring-link'),
    path('login/', views.obtain_auth_token),
    path('image/upload', ImageViewSet.as_view(), name='upload')
    #path('image/upload', uploadImage, name='upload')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 