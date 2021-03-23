from django import forms
from django.contrib.auth.models import User

class UnitCreateForm(forms.Form):
    uniqueid = forms.CharField(max_length=50,required=True,label='Identificador unico')
    imei = forms.CharField(max_length=50,required=True,label='Imei del equipo')
    sim_phonenumber = forms.CharField(max_length=50,required=False,label='Numero de telefono del sim')
    sim_iccid = forms.CharField(max_length=50,required=False,label='Identificador del sim')
    unit_name = forms.CharField(max_length=50,required=True,label='Placa de la unidad')

class UnitUpdateForm(forms.Form):
    uniqueid = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly'}),
        label='Identificador unico'
    )
    imei = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'readonly':'readonly'}),
        label='Imei del equipo'
    )
    sim_phonenumber = forms.CharField(max_length=50,required=True,label='Numero de telefono del sim')
    sim_iccid = forms.CharField(max_length=50,required=True,label='Identificador del sim')
    unit_name = forms.CharField(max_length=50,required=True,label='Placa de la unidad')