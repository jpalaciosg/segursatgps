from django import forms

class AlertHistoryForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=True,label='Unidad')
    alert_type = forms.IntegerField(label="Tipo de alerta")
