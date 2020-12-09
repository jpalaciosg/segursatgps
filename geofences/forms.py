from django import forms

class GeofenceCreateForm(forms.Form):
    name = forms.CharField(max_length=50,required=True,label='Nombre de la geocerca')
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}),required=False,label='Descripcion')
    geojson = forms.CharField(widget=forms.Textarea,label='Dibujar geocerca')