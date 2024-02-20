from django.urls import path
from api import views
from api.views import *


urlpatterns = [
    path('inventory/dashboard-01', views.inventory_dashboard_01),
    path('inventory/dashboard-02', views.inventory_dashboard_02),
    path('inventory/dashboard-03', views.inventory_dashboard_03),
    path('inventory/dashboard-04', views.inventory_dashboard_04),
    path('inventory/dashboard-05', views.inventory_dashboard_05),
    path('ipplan/dashboard-01', views.ipplan_dashboard_01),
    path('ipplan/dashboard-02', views.ipplan_dashboard_02),
    path('get-list-device', views.get_list_device),
    path('update-device-check-config', views.update_device_check_config),
    path('update-device-check-monitor', views.update_device_check_monitor)
]
