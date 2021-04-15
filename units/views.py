from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
from datetime import datetime
from pytz import timezone

from .models import Device
from .forms import UnitCreateForm,UnitUpdateForm
from .serializers import DeviceSerializer
from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor() #conversor zona horaria

# Create your views here.  
@login_required
def units_view(request):
    if request.method == 'POST':
        data = request.POST
        # Unit create
        if data['form_type'] == 'create_form':
            units = Device.objects.filter(account=request.user.profile.account)
            create_form = UnitCreateForm(data)
            if create_form.is_valid():
                data = create_form.cleaned_data
                try:
                    unit = Device.objects.get(
                        name = data['unit_name'],
                        account = request.user.profile.account
                    )
                except Device.DoesNotExist:
                    unit = None
                if unit:
                    create_form.add_error('unit_name', 'La unidad ya existe.')
                if not unit:
                    try:
                        unit = Device.objects.create(
                            name = data['unit_name'],
                            uniqueid = data['uniqueid'],
                            imei = data['imei'],
                            sim_phonenumber = data['sim_phonenumber'],
                            sim_iccid = data['sim_iccid'],
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
                        field = e.args[1].split('.')[1].replace("'","")
                        if field == 'imei': 
                            create_form.add_error('imei', 'imei ya existe.')
                        if field == 'uniqueid': 
                            create_form.add_error('uniqueid', 'identificador unico ya existe.')
            return render(request,'units/units.html',{
                'units':units,
                'create_form':create_form
            })
        # Unit update
        if data['form_type'] == 'update_form':
            units = Device.objects.filter(account=request.user.profile.account)
            create_form = UnitCreateForm()
            update_form = UnitUpdateForm(data,auto_id=False)
            if update_form.is_valid():
                form_data = update_form.cleaned_data
                try:
                    unit = Device.objects.get(
                        id=form_data['id'],
                        account=request.user.profile.account,
                    )
                except Device.DoesNotExist:
                    unit = None
                if unit:
                    try:
                        unit.name = form_data['unit_name']
                        unit.uniqueid = form_data['uniqueid']
                        unit.imei = form_data['imei']
                        unit.sim_phonenumber = form_data['sim_phonenumber']
                        unit.sim_iccid = form_data['sim_iccid']
                        unit.save()
                        return render(request,'units/units.html',{
                            'units':units,
                            'create_form':create_form,
                            'update_form':update_form,
                            'success':'Unidad actualizada exitosamente.'
                        })
                    except IntegrityError as e:
                        print(e)
                        field = e.args[1].split('.')[1].replace("'","")
                        if field == 'imei': 
                            update_form.add_error('imei', 'imei ya existe.')
                        if field == 'uniqueid': 
                            update_form.add_error('uniqueid', 'identificador unico ya existe.')
                    return render(request,'units/units.html',{
                        'units':units,
                        'create_form':create_form,
                        'update_form':update_form,
                        'modal_id':f'unit{unit.id}_update_modal',
                        'modal_unit_id':unit.id
                    })
                else:
                    return HttpResponse(status=500)
            else:
                try:
                    unit = Device.objects.get(
                        id=data['id'],
                        account=request.user.profile.account,
                    )
                except Device.DoesNotExist:
                    unit = None
                if unit:
                    return render(request,'units/units.html',{
                        'units':units,
                        'create_form':create_form,
                        'update_form':update_form,
                        'modal_id':f'unit{unit.id}_update_modal',
                        'modal_unit_id':unit.id
                    })
                else:
                    return HttpResponse(status=500)
                     
    # GET
    create_form = UnitCreateForm()
    units = Device.objects.filter(account=request.user.profile.account)
    for unit in units:
        try:
            unit.created = unit.created.replace(tzinfo=timezone('America/Lima'))
            unit.modified = unit.modified.replace(tzinfo=timezone('America/Lima'))
        except Exception as e:
            print(e)
    return render(request,'units/units.html',{
        'units':units,
        'create_form':create_form
    })

@api_view(['GET'])
def get_units(request):
    try:
        units = Device.objects.filter(account=request.user.profile.account)
        serializer = DeviceSerializer(units,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_unit(request,name):
    try:
        unit = Device.objects.get(name=name,account=request.user.profile.account)
        serializer = DeviceSerializer(unit,many=False)
        data = serializer.data
        try:
            data['last_attributes'] = json.loads(data['last_attributes'])
        except:
            data['last_attributes'] = ''
        last_report = datetime.fromtimestamp(unit.last_timestamp)
        last_report = gmt_conversor.convert_utctolocaltime(last_report)
        data['last_report'] = last_report.strftime("%d-%m-%Y %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def delete_unit(request,id):
    try:
        unit = Device.objects.get(id=id,account=request.user.profile.account)
        unit.delete()
        return redirect('units')
    except:
        return redirect('units')

@api_view(['GET'])
def get_unit_information(request,name):
    try:
        unit = Device.objects.get(name=name,account=request.user.profile.account)
        serializer = DeviceSerializer(unit,many=False)
        data = serializer.data
        try:
            data['last_attributes'] = json.loads(data['last_attributes'])
        except:
            data['last_attributes'] = ''
        data['last_report'] = datetime.fromtimestamp(unit.last_timestamp)
        data['last_report'] = gmt_conversor.convert_utctolocaltime(unit.last_report)
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)