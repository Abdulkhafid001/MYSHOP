from django import forms
from .models import UploadedImage, Players


class PlayerInfoForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = '__all__'
