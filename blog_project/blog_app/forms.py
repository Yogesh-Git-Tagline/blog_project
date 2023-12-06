from django import forms
from .models import BlogComment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['description']

    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Provide comment...🤔'}), label='')


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
        }

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }), label='Create Password')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }), label='Retype Password')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}),label='🙎🏻‍♂️ Enter username')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),label='🗝 Enter password')
