from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from common.privilege import Privilege

privilege = Privilege()

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

@login_required
def mobile_map_view(request):
    units = privilege.get_units(request)
    return render(request,'maps/mobile.html',{
        'units':units,
    })

@login_required
def multiple_unit_map_4_view(request):
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    number_of_maps = 4
    return render(request,'maps/multiple-map.html',{
        'navbar':navbar,
        'number_of_maps':number_of_maps,
    })

@login_required
def multiple_unit_map_6_view(request):
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    number_of_maps = 6
    return render(request,'maps/multiple-map.html',{
        'navbar':navbar,
        'number_of_maps':number_of_maps,
    })

@login_required
def multiple_unit_map_8_view(request):
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    number_of_maps = 8
    return render(request,'maps/multiple-map.html',{
        'navbar':navbar,
        'number_of_maps':number_of_maps,
    })
