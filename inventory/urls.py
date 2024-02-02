from django.urls import path
from inventory import views
from inventory.views import *
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('create-multiple-device', views.create_multiple_device),
    path('create-device', DeviceBasicInfoCreateView.as_view()),
    path('create-device-location', DeviceLocationCreateView.as_view()),
    path('create-device-type', DeviceTypeCreateView.as_view()),
    path('create-device-category', DeviceCategoryCreateView.as_view()),
    path('create-device-vendor', DeviceVendorCreateView.as_view()),
    path('list-device/device-basic-info', DeviceBasicInfoListView.as_view()),
    path('list-device/device-basic-info/delete/<int:pk>', DeviceBasicInfoDeleteView.as_view()),
    path('list-device/device-basic-info/update/<int:pk>', DeviceBasicInfoUpdateView.as_view()),
    path('list-device/device-basic-info/detail/<int:pk>', DeviceBasicInfoDetailView.as_view()),
    path('list-device/device-management', DeviceManagementListView.as_view()),
    path('list-device/device-management/update/<int:pk>', DeviceManagementUpdateView.as_view()),
    path('list-device/device-management/detail/<int:pk>', DeviceManagementDetailView.as_view()),
    path('list-device/device-topology', DeviceTopologyListView.as_view()),
    path('list-device/device-topology/update/<int:pk>', DeviceTopologyUpdateView.as_view()),
    path('list-device/device-topology/detail/<int:pk>', DeviceTopologyDetailView.as_view()),
    path('list-device/device-configuration', DeviceConfigurationListView.as_view()),
    path('list-device/device-interface', DeviceInterfaceListView.as_view()),
    path('list-device/device-interface/detail/<int:pk>', DeviceInterfaceDetailView.as_view()),
    path('device-dashboard', views.device_dashboard),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog')
]
