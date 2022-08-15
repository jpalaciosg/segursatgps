from django import forms

class DriverCreateForm(forms.Form):
    id = forms.CharField(max_length=50,required=True,label='Documento de identidad')
    lastname = forms.CharField(max_length=200,required=True,label='Apellidos')
    firstname = forms.CharField(max_length=200,required=True,label='Nombres')

class DriverUpdateForm(forms.Form):
    id = forms.CharField(max_length=50,required=True,label='Documento de identidad')
    lastname = forms.CharField(max_length=200,required=True,label='Apellidos')
    firstname = forms.CharField(max_length=200,required=True,label='Nombres')