from rest_framework import serializers
from .models import Image, UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

# connect models inside this serializer
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('user', 'image', 'thumbnail_200', 'thumbnail_400', 'expiration_time')
    expiration_time = serializers.IntegerField(min_value=300, max_value=30000, required=False)


    def create(self, validated_data):
        # Save the uploaded image
        image = validated_data.pop('image')
        user = validated_data.pop('user')
        instance = super().create(validated_data)
        instance.image = image

        for size in user.tier.size:
          print(size)


        instance.save()

        # # Generate thumbnails based on the user's plan
        # if instance.user.tier == Image.UNRESTRICTED:
        #     tier = instance.user.unrestricted
        #     # Save thumbnail for basic plan
        # else:
        #   if instance.user.tier in [Image.PREMIUM, Image.ENTERPRISE]:
        #       instance.thumbnail_400.save(image.name, image, save=False)
        #   instance.thumbnail_200.save(image.name, image, save=False)
        #   instance.save()


        return instance

    def update(self, instance, validated_data):
        # Update the expiration time if specified
        if 'expiration_time' in validated_data:
            instance.expiration_time = validated_data.pop('expiration_time')
            instance.save()

        return super().update(instance, validated_data)