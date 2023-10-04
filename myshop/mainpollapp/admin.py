from django.contrib import admin
from .models import ElectionResult
from .models import CandidateInfo
# Register your models here.
# to register our model
admin.site.register(ElectionResult)
admin.site.register(CandidateInfo)