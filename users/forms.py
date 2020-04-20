from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2',
                                                             'placeholder': 'Username*'}))
    first_name = forms.CharField(label='', max_length=100,
                                 widget=forms.TextInput(attrs={
                                                        'class': 'form-control  rounded-pill custom-input mb-2',
                                                        'placeholder': 'First Name*'}))
    last_name = forms.CharField(label='', max_length=100,
                                widget=forms.TextInput(attrs={
                                                       'class': 'form-control  rounded-pill custom-input mb-2',
                                                       'placeholder': 'Last Name'}),
                                required=False)
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control  rounded-pill custom-input mb-2',
               'placeholder': 'Email*'}))
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2',
                                                                  'placeholder': 'Password*'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2',
                                                                  'placeholder': 'Confirm Password*'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2', 'placeholder': 'Username*'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2', 'placeholder': 'Password*'}))


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2',
                                                             'placeholder': 'Username*'}))
    first_name = forms.CharField(label='', max_length=100,
                                 widget=forms.TextInput(attrs={
                                                        'class': 'form-control  rounded-pill custom-input mb-2',
                                                        'placeholder': 'First Name*'}))
    last_name = forms.CharField(label='', max_length=100,
                                widget=forms.TextInput(attrs={
                                                       'class': 'form-control  rounded-pill custom-input mb-2',
                                                       'placeholder': 'Last Name'}),
                                required=False)
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control  rounded-pill custom-input mb-2',
               'placeholder': 'Email*'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
