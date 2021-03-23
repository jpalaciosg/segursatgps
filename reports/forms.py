from django import forms

class ReportForm(forms.Form):
    initial_date = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_date = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=False,label='Unidad')