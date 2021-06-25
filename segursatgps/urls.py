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
import locations.views as locations_views
import maintenances.views as maintenances_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('users/', users_views.users_view, name='users'),
    path('users/delete-user/<str:username>/', users_views.delete_user, name='delete-user'),
    path('units/', units_views.units_view, name='units'),
    path('units/groups/', units_views.unit_group_view, name='unit-group'),
    path('units/delete-unit/<int:id>/', units_views.delete_unit, name='delete-unit'),
    path('drivers/', drivers_views.drivers_view, name='drivers'),
    path('drivers/delete-driver/<int:id>/', drivers_views.delete_driver, name='delete-driver'),
    path('geofences/', geofences_views.geofences_view, name='geofences'),
    path('geofences/delete-geofence/<int:id>/', geofences_views.delete_geofence, name='delete-geofence'),
    path('dashboard/', reports_views.dashboard_view, name='dashboard'),
    path('reports/fleet-status/', reports_views.fleet_status_view, name='fleet-status'),
    path('reports/detailed-report/', reports_views.detailed_report_view, name='detailed-report'),
    path('reports/speed-report/', reports_views.speed_report_view, name='speed-report'),
    path('reports/group-speed-report/', reports_views.group_speed_report_view, name='group-speed-report'),
    path('reports/travel-report/', reports_views.travel_report_view, name='travel-report'),
    path('reports/group-trip-report/', reports_views.group_trip_report_view, name='group-trip-report'),
    path('reports/stop-report/', reports_views.stop_report_view, name='stop-report'),
    path('reports/group-stop-report/', reports_views.group_stop_report_view, name='group-stop-report'),
    path('reports/mileage-report/', reports_views.mileage_report_view, name='mileage-report'),
    path('reports/group-mileage-report/', reports_views.group_mileage_report_view, name='group-mileage-report'),
    path('reports/geofence-report/', reports_views.geofence_report_view, name='geofence-report'),
    path('reports/group-geofence-report/', reports_views.group_geofence_report_view, name='group-geofence-report'),
    path('maps/', maps_views.map_view, name='map'),
    path('alerts/', alerts_views.alerts_view, name='alerts'),
    path('alerts/triggers/', alerts_views.triggers_view, name='triggers'),
    path('alerts/delete-trigger/<int:id>/', alerts_views.delete_trigger, name='delete-trigger'),
    path('alerts/history/', alerts_views.alert_history_view, name='alert-history'),
    path('maintenances/', maintenances_views.maintenances_view, name='maintenances'),
    path('maintenances/triggers/', maintenances_views.triggers_view, name='maintenance-triggers'),
    path('maintenances/history/', maintenances_views.maintenance_history_view, name='maintenance-history'),
    # REST FRAMEWORK
    path('web/api/units/get-units/', units_views.get_units),
    path('web/api/units/get-unit/<str:name>/', units_views.get_unit),
    path('web/api/units/get-unit-status/<str:name>/', units_views.get_unit_status),
    path('web/api/drivers/get-drivers/', drivers_views.get_drivers),
    path('web/api/drivers/get-driver/<int:id>/', drivers_views.get_driver),
    path('web/api/geofences/get-geofences/', geofences_views.get_geofences),
    path('web/api/geofences/get-geofence/<int:id>/', geofences_views.get_geofence),
    path('web/api/alerts/alert-search/<str:alert_date>/<str:unit_name>/', alerts_views.alert_search),
    path('web/api/alerts/get-alert/<int:id>/', alerts_views.get_alert),
    path('web/api/locations/insert-location/', locations_views.insert_location),
    path('web/api/locations/insert-location-batch/', locations_views.insert_location_batch),
    path('web/api/locations/get-location-history/<str:unit_name>/<str:initial_datetime>/<str:final_datetime>/', locations_views.get_location_history),
]
