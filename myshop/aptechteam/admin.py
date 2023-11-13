from django.contrib import admin
# import my models for the team app
from .models import Members, UploadedImage
# Register your models here.
# register the team model to admin panel to access django admin capabilities
admin.site.register(Members)
admin.site.register(UploadedImage)
