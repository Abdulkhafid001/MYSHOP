from django.db import models

# Create your models here.


class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=20, null=True)
    player_image = models.ImageField(upload_to='', null=True, width_field=40, height_field=40)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
