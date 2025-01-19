from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['username', 'image']