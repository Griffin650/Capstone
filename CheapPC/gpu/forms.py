from django import forms

from .models import User


# ModelForm for User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


def register_user(email, password):
    new_user = User(email=email, password=password)
    new_user.save()


class NewUser(forms.Form):
    newEmail = forms.CharField(label='email', max_length=100)
    newPassword = forms.CharField(label='password', max_length=100)
    repeat_newPassword = forms.CharField(label='repeat password', max_length=100)
