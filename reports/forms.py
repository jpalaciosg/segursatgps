from django import forms

class ReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=True,label='Unidad')

class SpeedReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=False,label='Unidad')
    speed_limit = forms.IntegerField(required=True)

class MileageReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')

class GeofenceReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=True,label='Unidad')
    geofence_name = forms.CharField(max_length=200,required=True,label='Geocerca')

class GroupReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    group_name = forms.CharField(max_length=50,required=True,label='Grupo')

class GroupSpeedReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    group_name = forms.CharField(max_length=50,required=True,label='Grupo')
    speed_limit = forms.IntegerField(required=True)

class DetailedMileageReportForm(forms.Form):
    initial_datetime = forms.CharField(max_length=50,required=True,label='Fecha inicial')
    final_datetime = forms.CharField(max_length=50,required=True,label='Fecha final')
    unit_name = forms.CharField(max_length=50,required=True,label='Unidad')
    mileage = forms.IntegerField(required=True)