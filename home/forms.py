from django.forms import ModelForm
from .models import *

class CropGuideForm(ModelForm):
    class Meta:
        model = CropGuide
        fields= '__all__'

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields= '__all__'
        exclude=['username']

class MarketPlaceForm(ModelForm):
    class Meta:
        model = Crop
        fields= '__all__'
        exclude=['username']
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'
        exclude=['user']