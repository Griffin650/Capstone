from django import forms

from .models import UserModel


# ModelForm for User
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
