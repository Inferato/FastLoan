from django import forms
from .user import User


class UserForm(forms.Form):
    username = forms.CharField(
        required=True,

    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
