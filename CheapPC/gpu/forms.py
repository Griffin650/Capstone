from django import forms

from .models import User


# ModelForm for User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
