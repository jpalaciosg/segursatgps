from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def map_view(request):
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    return render(request,'maps/map.html',{
        'navbar':navbar,
    })