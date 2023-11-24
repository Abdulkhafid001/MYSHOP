from django.contrib import admin
# import my models for the team app
from .models import Players, UploadedImage
# Register your models here.
# register the team model to admin panel to access django admin capabilities
# use admin ID functionality to get each image ID
class UploadedImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Players)
admin.site.register(UploadedImage, UploadedImageAdmin)
