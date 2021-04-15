from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from units.models import Device
from .forms import MaintenanceTriggerForm
from .models import MaintenaceTrigger

# Create your views here.
@login_required
def maintenances_view(request):
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'maintenances/maintenances.html',{
        'units': units,
    })

def triggers_view(request):
    #POST
    if request.method == 'POST':
        data = request.POST
        if data['form_type'] == 'create_form':
            units = Device.objects.filter(account=request.user.profile.account)
            maintenance_triggers = MaintenaceTrigger.objects.filter(account=request.user.profile.account)
            create_form = MaintenanceTriggerForm(data)
            if create_form.is_valid():
                form_data = create_form.cleaned_data
                try:
                    unit = Device.objects.get(
                        name=form_data['unit_name'],
                        account=request.user.profile.account
                    )
                except Device.DoesNotExist:
                    unit = None
                if unit == None:
                    create_form.add_error('unit_name', 'La unidad no existe.')
                else:
                    MaintenaceTrigger.objects.create(
                        name = form_data["name"],
                        unit = unit,
                        description = form_data["description"],
                        programing_type = form_data["programing_type"],
                        programing = form_data["programing"],
                        is_active = form_data["is_active"],
                        account = unit.account
                    )
                    return render(request,'maintenances/triggers.html',{
                        'units':units,
                        'maintenance_triggers':maintenance_triggers,
                        'create_form':create_form,
                        'success':'trigger creado exitosamente.'
                    })
            return render(request,'maintenances/triggers.html',{
                'units':units,
                'maintenance_triggers':maintenance_triggers,
                'create_form':create_form,
            })
    # GET
    create_form = MaintenanceTriggerForm()
    units = Device.objects.filter(account=request.user.profile.account)
    maintenance_triggers = MaintenaceTrigger.objects.filter(account=request.user.profile.account)
    return render(request,'maintenances/triggers.html',{
        'units': units,
        'maintenance_triggers':maintenance_triggers,
        'create_form': create_form
    })

def maintenance_history_view(request):
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'maintenances/maintenance-history.html',{
        'units': units,
    })