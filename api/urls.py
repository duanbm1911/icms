from django.urls import path
from api import views
from api.views import *


urlpatterns = [
    path('inventory/dashboard-01', views.inventory_dashboard_01),
    path('inventory/dashboard-02', views.inventory_dashboard_02),
    path('inventory/dashboard-03', views.inventory_dashboard_03),
    path('inventory/dashboard-04', views.inventory_dashboard_04),
    path('inventory/dashboard-05', views.inventory_dashboard_05),
    path('inventory/dashboard-06', views.inventory_dashboard_06),
    path('inventory/dashboard-07', views.inventory_dashboard_07),
    path('inventory/report', views.inventory_report),
    path('ipplan/dashboard-01', views.ipplan_dashboard_01),
    path('ipplan/dashboard-02', views.ipplan_dashboard_02),
    path('get-list-device', views.get_list_device),
    path('update-device-check-config', views.update_device_check_config),
    path('update-device-check-monitor', views.update_device_check_monitor),
    path('update-device-firmware', views.update_device_firmware),
    path('update-device-interface', views.update_device_interface),
    path('update-device-status', views.update_device_status),
    path('cm/checkpoint/create-rule', views.cm_checkpoint_create_rule),
    path('cm/checkpoint/get-list-policy', views.cm_checkpoint_get_list_policy),
    path('cm/checkpoint/get-list-rule', views.cm_checkpoint_get_list_rule),
    path('cm/checkpoint/update-rule-status', views.cm_checkpoint_update_rule_status),
    path('cm/f5/get-list-device', views.cm_f5_get_list_device),
    path('cm/f5/create-virtual-server', views.cm_f5_create_virtual_server),
    path('cm/f5/get-list-client-ssl-profile', views.f5_get_list_client_ssl_profile),
    path('cm/f5/get-list-server-ssl-profile', views.f5_get_list_server_ssl_profile),
    path('cm/f5/update-client-ssl-profile', views.f5_update_client_ssl_profile),
    path('cm/f5/update-server-ssl-profile', views.f5_update_server_ssl_profile),
    path('cm/f5/update-irule-profile', views.f5_update_irule_profile),
    path('cm/f5/update-waf-profile', views.f5_update_waf_profile),
    path('cm/f5/get-list-template', views.f5_get_list_template),
    path('cm/f5/get-list-virtual-server', views.f5_get_list_virtual_server),
    path('cm/f5/update-virtual-server-status', views.f5_update_virtual_server_status)
]