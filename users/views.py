from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#from django.contrib.auth.models import User
from users.models import User
from .models import Account, Profile
from .forms import UserCreateForm,UserUpdateForm
from .serializers import AccountSerializer,ProfileSerializer

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.user.is_staff:
                return redirect('management-dashboard')
            try:
                profile = request.user.profile
            except:
                profile = None
            if profile:
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('main')
            logout(request)
            return render(request,'users/login.html',{
                'error':'No existe cuenta vinculada a este usuario, contactese con el administrador',
            })
        else:
            return render(request,'users/login.html',{'error':'Usuario y/o contraseña invalidos'})
    try:
        account = request.GET['account']
    except:
        account = None
    if account == "autoplan":
        return render(request,'users/login-autoplan.html')
    if account == "civa":
        return render(request,'users/login-civa.html')
    if account == "renting":
        return render(request,'users/login-renting.html')
    
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def users_view(request):
    # verificar privilegios
    if privilege.view_latest_alerts(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        # create form
        if data['form_type'] == 'create_form':
            profiles = Profile.objects.filter(account=request.user.profile.account)
            create_form = UserCreateForm(data)
            if create_form.is_valid():
                form_data = create_form.cleaned_data
                try:
                    user = User.objects.get(username=form_data['username'])
                except User.DoesNotExist:
                    user = None
                if user:
                    create_form.add_error('username', 'El usuario ya existe.')
                else:
                    if form_data['password'] != form_data['password_confirmation']:
                        create_form.add_error('password', 'La contraseña no coincide.')
                        create_form.add_error('password_confirmation', 'La contraseña no coincide.')
                    else:
                        user = User.objects.create_user(
                            username = form_data['username'],
                            email = form_data['username'],
                            first_name = form_data['firstname'],
                            last_name = form_data['lastname'],
                            password = form_data['password']
                        )
                        profile = Profile.objects.create(
                            user = user,
                            account = request.user.profile.account
                        )
                        return render(request,'users/users.html',{
                            'profiles':profiles,
                            'create_form':create_form,
                            'success':'Usuario creado exitosamente.'
                        })
            return render(request,'users/users.html',{
                'profiles':profiles,
                'create_form':create_form
            })
        # update form
        if data['form_type'] == 'update_form':
            profiles = Profile.objects.filter(account=request.user.profile.account)
            create_form = UserCreateForm()
            update_form = UserUpdateForm(data,auto_id=False)
            try:
                user = User.objects.get(username=data['username'])
            except User.DoesNotExist:
                user = None
            if update_form.is_valid():
                form_data = update_form.cleaned_data
                if user == None:
                    update_form.add_error('username', 'El usuario no existe.')
                if user:
                    try:
                        user.first_name = form_data['firstname']
                        user.last_name = form_data['lastname']
                        user.is_active = form_data['is_active']
                        user.save()
                        return render(request,'users/users.html',{
                            'profiles':profiles,
                            'create_form':create_form,
                            'update_form':update_form,
                            'success':'Usuario actualizado exitosamente.'
                        })
                    except Exception as e:
                        print(e)
                return render(request,'users/users.html',{
                    'profiles':profiles,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'{user}_update_modal',
                    'modal_user_id':user
                })
            else:
                return render(request,'users/users.html',{
                    'profiles':profiles,
                    'create_form':create_form,
                    'update_form':update_form,
                    'modal_id':f'{user}_update_modal',
                    'modal_user_id':user
                })
    # GET
    profiles = Profile.objects.filter(account=request.user.profile.account)
    create_form = UserCreateForm()
    for profile in profiles:
        try:
            #profile.user.last_login = profile.user.last_login.replace(tzinfo=timezone('America/Lima'))
            profile.user.last_login = gmt_conversor.convert_localtimetoutc(profile.user.last_login)
        except Exception as e:
            print(e)
    return render(request,'users/users.html',{
        'profiles':profiles,
        'create_form':create_form,
    })

@api_view(['GET'])
def get_users(request):
    profiles = Profile.objects.filter(account=request.user.profile.account)
    serializer = ProfileSerializer(profiles,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(profiles[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(profiles[i].modified).strftime("%d/%m/%Y %H:%M:%S")
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request,id):
    try:
        profile = Profile.objects.get(id=id,account=request.user.profile.account)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(profile,many=False)
    data = serializer.data
    return Response(data,status=status.HTTP_200_OK)