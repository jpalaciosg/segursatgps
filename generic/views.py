from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main_view(request):
    profile = request.user.profile
    return render(request,'generic/main.html',{
        'profile': profile,
    })