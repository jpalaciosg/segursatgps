from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import BSModalFormView

from .models import Profile
from .forms import UserCreateForm,UserUpdateForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            try:
                account = request.user.profile.account
            except:
                logout(request)
                return render(request,'users/login.html',{
                    'error':'No existe cuenta vinculada a este usuario, contactese con el administrador',
                })
            return redirect('map')
        else:
            return render(request,'users/login.html',{'error':'Usuario y/o contraseña invalidos'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def users_view(request):
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
    return render(request,'users/users.html',{
        'profiles':profiles,
        'create_form':create_form,
    })

@login_required
def delete_user(request,username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return redirect('users')
    except:
        return redirect('users')