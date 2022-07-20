from django.contrib import admin



# Register your models here.
from .models import *

admin.site.register(Developer)
admin.site.register(Blog)
admin.site.register(CropGuide)
admin.site.register(Profile)
admin.site.register(Crop)
admin.site.register(Purchase)
admin.site.register(Comment)