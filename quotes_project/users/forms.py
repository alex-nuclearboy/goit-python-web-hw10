from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.

    Attributes:
        username (CharField): Field for the user's username.
        password1 (CharField): Field for the password, with input masked.
        password2 (CharField): Field for confirming the password, also masked.
    """
    username = forms.CharField(min_length=5,
                               max_length=100,
                               required=True,
                               widget=forms.TextInput())
    password1 = forms.CharField(min_length=6,
                                max_length=25,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=6,
                                max_length=25,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """
    A form for logging in users. Inherits from Django's AuthenticationForm,
    which itself handles authentication logic.
    """
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    """
    A form for editing a user's profile.
    Specifically handles the upload of user avatars.

    Attributes:
        avatar (ImageField): Field for uploading an avatar image.
    """
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = fields = ['avatar', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date']
