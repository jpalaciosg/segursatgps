from .models import Driver
from bootstrap_modal_forms.forms import BSModalModelForm

class DriverModelForm(BSModalModelForm):
    class Meta:
        model = Driver
        fields = ['id','firstname','lastname','account']
        labels = {
            'id':'Numero de DNI',
            'firstname':'Nombres',
            'lastname':'Apellidos',
        }