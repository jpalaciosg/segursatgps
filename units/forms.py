from django import forms
from django.contrib.auth.models import User

class UnitCreateForm(forms.Form):
    uniqueid = forms.CharField(max_length=50,required=True,label='Identificador unico')
    imei = forms.CharField(max_length=50,required=True,label='Imei del equipo')
    sim_phonenumber = forms.CharField(max_length=50,required=False,label='Numero de telefono del sim')
    sim_iccid = forms.CharField(max_length=50,required=False,label='Identificador del sim')
    unit_name = forms.CharField(max_length=50,required=True,label='Placa de la unidad')
    description = forms.CharField(max_length=200,required=False,label='Descripción de la unidad')
    note = forms.CharField(widget=forms.Textarea,required=False,label='Nota')

class UnitUpdateForm(forms.Form):
    id = forms.IntegerField(required=True,widget=forms.HiddenInput())
    uniqueid = forms.CharField(max_length=50,required=True,label='Identificador unico')
    imei = forms.CharField(max_length=50,required=True,label='Imei del equipo')
    sim_phonenumber = forms.CharField(max_length=50,required=True,label='Numero de telefono del sim')
    sim_iccid = forms.CharField(max_length=50,required=True,label='Identificador del sim')
    unit_name = forms.CharField(max_length=50,required=True,label='Placa de la unidad')
    description = forms.CharField(max_length=200,required=False,label='Descripción de la unidad')
    odometer = forms.DecimalField(required=True,label='Odometro')
    note = forms.CharField(widget=forms.Textarea,required=False,label='Nota')