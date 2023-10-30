from django.shortcuts import render
from django.http import JsonResponse
from inventory.models import *
from ipplan.models import *

# Create your views here.

def inventory_dashboard_01(request):
    """
    This dashboard will be display count of device by category
    """
    category_count = list()
    list_category = list(DeviceCategory.objects.values_list('device_category', flat=True))
    for obj in list_category:
        count = DeviceBasicInfo.objects.filter(device_category__device_category=obj).count()
        category_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': category_count})


def inventory_dashboard_02(request):
    """
    This dashboard will be display count of device by vendor
    """
    vendor_count = list()
    list_vendor = list(DeviceVendor.objects.values_list('device_vendor', flat=True))
    for obj in list_vendor:
        count = DeviceBasicInfo.objects.filter(device_vendor__device_vendor=obj).count()
        vendor_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': vendor_count})


def inventory_dashboard_03(request):
    """
    This dashboard will be display count of device by vendor
    """
    location_count = list()
    list_vendor = list(DeviceLocation.objects.values_list('device_location', flat=True))
    for obj in list_vendor:
        count = DeviceBasicInfo.objects.filter(device_location__device_location=obj).count()
        location_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': location_count})


def inventory_dashboard_04(request):
    """
    This dashboard will be display count of device by vendor
    """
    type_count = list()
    list_vendor = list(DeviceType.objects.values_list('device_type', flat=True))
    for obj in list_vendor:
        count = DeviceBasicInfo.objects.filter(device_type__device_type=obj).count()
        type_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': type_count})
