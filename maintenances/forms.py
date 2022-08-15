from django import forms

class MaintenanceTriggerForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,label='Nombre del disparador')
    unit_name = forms.CharField(max_length=100,required=True,label='Unidad')
    programing_type = forms.CharField(max_length=100,required=True,label='Tipo de programación')
    programing = forms.CharField(max_length=100,required=True,label='Programación')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}),required=False,label='Descripcion')
    is_active = forms.BooleanField(label='Esta activo?')