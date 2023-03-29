from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Image, Thumbnail
from .serializers import ImageSerializer
from django.http import HttpResponse
import json
from PIL import Image as PilImage

class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
      
      images = Image.objects.filter(user=self.request.user)
      # ret = {}
      # for image in images:
      #   ret[image.image.name] = {}
      #   ret[image.image.name]['link'] = image.original_link
      #   ret[image.image.name]['thumbnails'] = Thumbnail.objects.filter(image=image).all().values()
      return images

class ImageViewSet(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES["file"]

        image = Image.objects.create(image=file, user=request.user)
        for size in request.user.user_tier.size.all():
          pi = PilImage.open(image.image)
          pi.show()
          pi.thumbnail((int(size.width), int(size.height)))
          #thumb = Thumbnail.objects.create(image=image, thumbnail=pi, size=size, original_link="asdf")
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


@api_view(['GET'])
def generate_expiring_link(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the user has permission to generate an expiring link
    if not request.user.is_staff and image.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    # Generate the link with the specified expiration time (if provided), or use the default
    expiration_time = request.query_params.get('expiration_time', None)
    link = image.generate_expiring_link(int(expiration_time) if expiration_time else None)

    return Response({'link': link})

