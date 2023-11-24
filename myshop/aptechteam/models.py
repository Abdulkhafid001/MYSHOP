from django.db import models

# Create your models here.


class Players(models.Model):
    player_name = models.CharField(max_length=255)
    position = models.CharField(max_length=20, null=True)
    player_image = models.ImageField(
        upload_to='images/', null=True, blank=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


class UploadedImage(models.Model):
    image_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='')
