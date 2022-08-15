from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Driver
from .forms import DriverCreateForm,DriverUpdateForm
from .serializers import DriverSerializer

# Create your views here.

@login_required
def drivers_view(request):
    if request.method == 'POST':
        data = request.POST
        # Create driver
        if data['form_type'] == 'create_form':
            drivers = Driver.objects.filter(account=request.user.profile.account)
            create_form = DriverCreateForm(data)
            if create_form.is_valid():
                form_data = create_form.cleaned_data
                try:
                    driver = Driver.objects.get(id=form_data['id'])
                except Driver.DoesNotExist:
                    driver = None
                if driver:
                    create_form.add_error('id', 'El numero de documento ya existe.')
                else:
                    driver = Driver.objects.create(
                        id = form_data['id'],
                        firstname = form_data['firstname'],
                        lastname = form_data['lastname'],
                        account = request.user.profile.account
                    )
                    return render(request,'drivers/drivers.html',{
                        'drivers':drivers,
                        'create_form':create_form,
                        'success':'conductor creado exitosamente.'
                    })
            return render(request,'drivers/drivers.html',{
                'drivers':drivers,
                'create_form':create_form
            })
        # Unit update
        if data['form_type'] == 'update_form':
            drivers = Driver.objects.filter(account=request.user.profile.account)
            create_form = DriverCreateForm()
            update_form = DriverUpdateForm(data,auto_id=False)
            try:
                driver = Driver.objects.get(id=data['id'])
            except Driver.DoesNotExist:
                driver = None
            if update_form.is_valid():
                form_data = update_form.cleaned_data
                if driver == None:
                    update_form.add_error('id', 'El dispositivo no existe.')
                if driver:
                    try:
                        driver.firstname = form_data['firstname']
                        driver.lastname = form_data['lastname']
                        driver.save()
                        return render(request,'drivers/drivers.html',{
                            'drivers':drivers,
                            'create_form':create_form,
                            'update_form':update_form,
                            'success':'Conductor actualizado exitosamente.'
                        })
                    except Exception as e:
                        print(e)
                return render(request,'drivers/drivers.html',{
                    'drivers':drivers,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'unit{driver.id}_update_modal',
                    'modal_driver_id':driver.id
                })
            else:
                return render(request,'drivers/drivers.html',{
                    'drivers':drivers,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'unit{driver.id}_update_modal',
                    'modal_driver_id':driver.id
                })
                   
    # GET
    create_form = DriverCreateForm()
    drivers = Driver.objects.filter(account=request.user.profile.account)
    return render(request,'drivers/drivers.html',{
        'drivers':drivers,
        'create_form':create_form,
    })

@api_view(['GET'])
def get_drivers(request):
    try:
        drivers = Driver.objects.filter(account=request.user.profile.account)
        serializer = DriverSerializer(drivers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_driver(request,id):
    try:
        driver = Driver.objects.get(id=id,account=request.user.profile.account)
        serializer = DriverSerializer(driver, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def delete_driver(request,id):
    try:
        driver = Driver.objects.get(id=id,account=request.user.profile.account)
        driver.delete()
        return redirect('drivers')
    except:
        return redirect('drivers')