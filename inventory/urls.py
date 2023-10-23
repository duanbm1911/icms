from django.urls import path
from inventory import views
from inventory.views import *


urlpatterns = [
    path('create-multiple-device', views.create_multiple_device),
    path('create-device', DeviceModelCreateView.as_view()),
    path('create-device-location', DeviceLocationCreateView.as_view()),
    path('create-device-type', DeviceTypeCreateView.as_view()),
    path('create-device-category', DeviceCategoryCreateView.as_view()),
    path('create-device-vendor', DeviceVendorCreateView.as_view()),
    path('update-device/<int:pk>', DeviceModelUpdateView.as_view()),
    path('detail-device/<int:pk>', DeviceModelDetailView.as_view()),
    path('delete-device/<int:pk>', DeviceModelDeleteView.as_view()),
    path('list-device', DeviceModelListView.as_view()),
    path('device-dashboard', views.device_dashboard)
]
