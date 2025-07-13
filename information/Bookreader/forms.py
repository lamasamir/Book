from django.forms import ModelForm,forms
from .models import Book,User_Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class style_bookform(ModelForm):
    class Meta:
        model = Book
        fields = ["title","genre","des","book_coverimage","author", "content_pdf"]


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search Books")


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label='Username',
        help_text=''  # Remove default hint
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='',  # Remove default hint
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='',  # Remove default hint
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")    



class UserForm(ModelForm):
    class Meta:
        model = User_Data
        fields = ['name','email']
    