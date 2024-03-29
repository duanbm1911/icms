from django.shortcuts import render
from django.http import JsonResponse
from inventory.models import *
from ipplan.models import *
import random

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
    This dashboard will be display count of configuration management
    """
    data_point_01 = list()
    data_point_02 = list()
    data_point_03 = list()
    list_data_point = [
    {
        "name": data_point_01,
        "desc": "Non-compliance configuration"
    },
    {
        "name": data_point_02,
        "desc": "Device no monitor"
    },
    {
        "name": data_point_03,
        "desc": "Device no backup configuration"
    }
    ]
    chart_data = list()
    list_vendor = list(DeviceVendor.objects.values_list('device_vendor', flat=True))
    for obj in list_vendor:
        point_01 = DeviceConfiguration.objects.filter(device_config_standardized=False, device_ip__device_vendor__device_vendor=obj).count()
        point_02 = DeviceConfiguration.objects.filter(device_monitored=False, device_ip__device_vendor__device_vendor=obj).count()
        point_03 = DeviceConfiguration.objects.filter(device_backup_config=False, device_ip__device_vendor__device_vendor=obj).count()
        data_point_01.append({
            'label': obj,
            'y': point_01
        })
        data_point_02.append({
            'label': obj,
            'y': point_02
        })
        data_point_03.append({
            'label': obj,
            'y': point_03
        })
    list_data_point = [{
        "name": data_point_01,
        "desc": "Non-compliance configuration"
    },
    {
        "name": data_point_02,
        "desc": "Device no monitor"
    },
    {
        "name": data_point_03,
        "desc": "Device no backup configuration"
    }]
    color = lambda: random.randint(0,255)
    for data_point in list_data_point:
        chart_data.append({
            "type": "line",
            "showInLegend": "true",
            "name": data_point['desc'],
            "markerSize": 0,
            "markerType": "square",
            "color": '#%02X%02X%02X' % (color(),color(),color()),
            "dataPoints": data_point['name']
        })
    return JsonResponse({'data': chart_data})

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

def inventory_dashboard_05(request):
    """
    This dashboard will be display count of device by vendor
    """
    location_count = list()
    list_location = list(DeviceLocation.objects.values_list('device_location', flat=True))
    for obj in list_location:
        count = DeviceBasicInfo.objects.filter(device_location__device_location=obj).count()
        location_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': location_count})
    
def ipplan_dashboard_01(request):
    """
    This dashboard will be display count of location by regoin
    """
    location_count = list()
    list_region = list(Region.objects.values_list('region', flat=True))
    for obj in list_region:
        count = Location.objects.filter(region__region=obj).count()
        location_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': location_count})

def ipplan_dashboard_02(request):
    """
    This dashboard will be display count of subnet by location
    """
    subnet_count = list()
    list_location = list(Location.objects.values_list('location', flat=True))
    for obj in list_location:
        count = Subnet.objects.filter(location__location=obj).count()
        subnet_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': subnet_count})