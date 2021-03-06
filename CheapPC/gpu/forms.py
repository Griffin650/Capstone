from django import forms


class NewUser(forms.Form):
    newEmail = forms.CharField(label='email', max_length=100)
    newPassword = forms.CharField(label='password', max_length=100)
    repeat_newPassword = forms.CharField(label='repeat password', max_length=100)