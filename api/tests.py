from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .models import Image


class ImageModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

    def test_image_creation(self):
        image = Image.objects.create(
            user=self.user,
            image=self.image,
            plan=Image.BASIC,
        )
        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.__str__(), image.image.name)

    def test_image_thumbnail_creation(self):
        image = Image.objects.create(
            user=self.user,
            image=self.image,
            plan=Image.PREMIUM,
        )
        self.assertIsNotNone(image.thumbnail_200)
        self.assertIsNotNone(image.thumbnail_400)

    def test_image_expiration_time(self):
        image = Image.objects.create(
            user=self.user,
            image=self.image,
            plan=Image.ENTERPRISE,
            expiration_time=600
        )
        self.assertEqual(image.expiration_time, 600)
