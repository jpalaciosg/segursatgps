from django import forms

class TriggerCreateForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,label='Nombre del disparador')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}),required=False,label='Descripcion')
    condition = forms.CharField(widget=forms.Textarea,label='Escribir json')
    is_active = forms.BooleanField(label='Esta activo?')