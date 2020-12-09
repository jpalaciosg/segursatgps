from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=50,required=True,label='Nombre de usuario')
    lastname = forms.CharField(max_length=200,required=True,label='Apellidos')
    firstname = forms.CharField(max_length=200,required=True,label='Nombres')
    password = forms.CharField(widget=forms.PasswordInput(),required=True,label='Ingresar contraseña')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(),required=True,label='Confirmar contraseña')
    