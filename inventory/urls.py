from django.urls import path
from inventory import views
from inventory.views import *


urlpatterns = [
    path('create-multiple-device', views.create_multiple_device),
    path('create-device', DeviceBasicInfoCreateView.as_view()),
    path('create-device-location', DeviceLocationCreateView.as_view()),
    path('create-device-type', DeviceTypeCreateView.as_view()),
    path('create-device-category', DeviceCategoryCreateView.as_view()),
    path('create-device-vendor', DeviceVendorCreateView.as_view()),
    path('update-device/<int:pk>', DeviceBasicInfoUpdateView.as_view()),
    path('detail-device/<int:pk>', DeviceBasicInfoDetailView.as_view()),
    path('delete-device/<int:pk>', DeviceBasicInfoDeleteView.as_view()),
    path('list-device/device-basic-info', DeviceBasicInfoListView.as_view()),
    path('list-device/device-management', DeviceManagementListView.as_view()),
    path('list-device/device-interface', DeviceInterfaceListView.as_view()),
    path('list-device/device-topology', DeviceTopologyListView.as_view()),
    path('list-device/device-configuration', DeviceConfigurationListView.as_view()),
    path('list-device/device-interface/detail/<int:pk>', DeviceInterfaceDetailView.as_view()),
    path('device-dashboard', views.device_dashboard)
]
