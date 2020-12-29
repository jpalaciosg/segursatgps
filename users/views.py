from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import BSModalFormView

from .models import Profile
from .forms import UserCreateForm

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
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = User.objects.get(username=data['username'])
            except User.DoesNotExist:
                user = None
            if user:
                form.add_error('username', 'El usuario ya existe.')
            else:
                user = User.objects.create(
                    username = data['username'],
                    first_name = data['firstname'],
                    last_name = data['lastname']
                )
                profile = Profile.objects.create(
                    user = user,
                    account = request.user.profile.account
                )
                return redirect('users')
    profiles = Profile.objects.filter(account=request.user.profile.account)
    return render(request,'users/users.html',{
        'profiles':profiles,
        'form':form,
    })

@login_required
def delete_user(request,username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return redirect('users')
    except:
        return redirect('users')