from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
from datetime import datetime

from .models import Unit,Device
from .serializers import UnitSerializer
from .forms import UnitCreateForm,UnitUpdateForm

# Create your views here.  
@login_required
def units_view(request):
    if request.method == 'POST':
        data = request.POST
        # Unit create
        if data['form_type'] == 'create_form':
            units = Unit.objects.filter(account=request.user.profile.account)
            create_form = UnitCreateForm(data)
            if create_form.is_valid():
                data = create_form.cleaned_data
                try:
                    device = Device.objects.get(uniqueid=data['uniqueid'])
                except Device.DoesNotExist:
                    device = None
                try:
                    unit = Unit.objects.get(name=data['unit_name'])
                except Unit.DoesNotExist:
                    unit = None
                if device:
                    create_form.add_error('uniqueid', 'El dispositivo ya existe.')
                if unit:
                    create_form.add_error('unit_name', 'La unidad ya existe.')
                if not device and not unit:
                    try:
                        device = Device.objects.create(
                            uniqueid = data['uniqueid'],
                            imei = data['imei'],
                            sim_phonenumber = data['sim_phonenumber'],
                            sim_iccid = data['sim_iccid']
                        )
                        unit = Unit.objects.create(
                            name = data['unit_name'],
                            device = device,
                            account = request.user.profile.account
                        )
                        create_form = UnitCreateForm()
                        return render(request,'units/units.html',{
                            'units':units,
                            'create_form':create_form,
                            'success':'Unidad creada exitosamente.'
                        })
                    except IntegrityError as e:
                        print(e)
                        field = e.args[0].split('.')[1]
                        if field == 'imei': 
                            create_form.add_error('imei', 'imei ya existe.')
            return render(request,'units/units.html',{
                'units':units,
                'create_form':create_form
            })
        # Unit update
        if data['form_type'] == 'update_form':
            units = Unit.objects.filter(account=request.user.profile.account)
            create_form = UnitCreateForm()
            update_form = UnitUpdateForm(data,auto_id=False)
            try:
                device = Device.objects.get(uniqueid=data['uniqueid'])
            except Device.DoesNotExist:
                device = None
            try:
                unit = Unit.objects.get(name=data['unit_name'])
            except Unit.DoesNotExist:
                unit = None

            if update_form.is_valid():
                form_data = update_form.cleaned_data
                if device == None:
                    update_form.add_error('uniqueid', 'El dispositivo no existe.')
                if unit == None:
                    update_form.add_error('unit_name', 'La unidad no existe.')
                if device and unit:
                    try:
                        device.sim_phonenumber = form_data['sim_phonenumber']
                        device.sim_iccid = form_data['sim_iccid']
                        unit.name = form_data['unit_name']
                        device.save()
                        unit.save()
                        return render(request,'units/units.html',{
                            'units':units,
                            'create_form':create_form,
                            'update_form':update_form,
                            'success':'Unidad actualizada exitosamente.'
                        })
                    except Exception as e:
                        print(e)
                return render(request,'units/units.html',{
                    'units':units,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'unit{unit.id}_update_modal',
                    'modal_unit_id':unit.id
                })
            else:
                return render(request,'units/units.html',{
                    'units':units,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'unit{unit.id}_update_modal',
                    'modal_unit_id':unit.id
                })
                     
    # GET
    create_form = UnitCreateForm()
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'units/units.html',{
        'units':units,
        'create_form':create_form
    })

@api_view(['GET'])
def get_units(request):
    try:
        units = Unit.objects.filter(account=request.user.profile.account)
        serializer = UnitSerializer(units,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_unit(request,name):
    try:
        unit = Unit.objects.get(name=name,account=request.user.profile.account)
        serializer = UnitSerializer(unit,many=False)
        data = serializer.data
        data['device']['last_attributes'] = json.loads(data['device']['last_attributes'])
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def delete_unit(request,id):
    try:
        unit = Unit.objects.get(id=id,account=request.user.profile.account)
        unit.device.delete()
        return redirect('units')
    except:
        return redirect('units')

@api_view(['GET'])
def get_unit_information(request,name):
    try:
        unit = Unit.objects.get(name=name,account=request.user.profile.account)
        serializer = UnitSerializer(unit,many=False)
        data = serializer.data
        data['device']['last_attributes'] = json.loads(data['device']['last_attributes'])
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)