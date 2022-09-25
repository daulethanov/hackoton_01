from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    firs_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))
    iin = forms.IntegerField(label='ИИН', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'firs_name', 'last_name', 'patronymic', 'iin', 'email', 'password1', 'password2', 'number')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'document', 'description',]


class CheckDocument(forms.ModelForm):

    class Meta:
        model = CheckDocument
        fields = ['document', 'plan', 'idea', 'actual', 'status', 'user']

