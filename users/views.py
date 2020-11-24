from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile

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
            return redirect('users')
        else:
            return render(request,'users/login.html',{'error':'Usuario y/o contraseña invalidos'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def users_view(request):
    profiles = Profile.objects.filter(account=request.user.profile.account)
    return render(request,'users/users.html',{
        'profiles':profiles,
    })

