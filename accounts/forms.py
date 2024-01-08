from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter Password'}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter Username'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'enter your email'
    }), required=False)
    first_name = forms.CharField(max_length=110, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your first name'}
    ))
    last_name = forms.CharField(max_length=110, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your first name'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter Password'}))

    password_2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter Password'}))

    def clean_username(self):
        username_input = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username_input).exists()
        if user_exists:
            raise ValidationError('This Username is taken by another user')
        return username_input

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 != password_2:
            raise ValidationError('Passwords not Match')
        return password_2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('This Email is Exists')
        return email