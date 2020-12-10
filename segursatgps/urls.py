"""segursatgps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import users.views as users_views
import units.views as units_views
import drivers.views as drivers_views
import geofences.views as geofences_views
import reports.views as reports_views
import maps.views as maps_views
import alerts.views as alerts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('users/', users_views.users_view, name='users'),
    path('units/', units_views.units_view, name='units'),
    path('drivers/', drivers_views.drivers_view, name='drivers'),
    path('geofences/', geofences_views.geofences_view, name='geofences'),
    path('dashboard/', reports_views.dashboard_view, name='dashboard'),
    path('maps/', maps_views.map_view, name='map'),
    path('alerts/', alerts_views.alerts_view, name='alerts'),
    path('alerts/triggers/', alerts_views.triggers_view, name='triggers'),
    path('alerts/history/', alerts_views.alert_history_view, name='alert-history'),
    # REST FRAMEWORK
    path('web/api/units/get-units/', units_views.get_units),
    path('web/api/drivers/get-drivers/', drivers_views.get_drivers),
    path('web/api/drivers/get-driver/<int:id>/', drivers_views.get_driver),
    path('web/api/geofences/get-geofences/', geofences_views.get_geofences),
    path('web/api/geofences/get-geofence/<str:name>/', geofences_views.get_geofence),
    path('web/api/alerts/alert-search/<str:alert_date>/<str:unit_name>/', alerts_views.alert_search),
    path('web/api/alerts/get-alert/<int:id>/', alerts_views.get_alert),
]
