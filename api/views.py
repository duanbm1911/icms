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
        count = DeviceBaseInfo.objects.filter(device_category__device_category=obj).count()
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
        count = DeviceBaseInfo.objects.filter(device_vendor__device_vendor=obj).count()
        vendor_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': vendor_count})