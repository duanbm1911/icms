from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from inventory.models import *
from ipplan.models import *
import random
import base64

# Create your views here.

def view_or_basicauth(view, request, test_func, realm = "", *args, **kwargs):

    if test_func(request.user):
        return view(request, *args, **kwargs)

    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:

            if auth[0].lower() == "basic":
                string = auth[1].encode('utf-8')
                secret = base64.b64decode(string).decode('utf-8')
                uname, passwd = secret.split(':')
                user = authenticate(username=uname, password=passwd)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.user = user
                        return view(request, *args, **kwargs)

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % realm
    return response

def logged_in_or_basicauth(realm = ""):

    def view_decorator(func):
        def wrapper(request, *args, **kwargs):
            return view_or_basicauth(func, request,
                                     lambda u: u.is_authenticated,
                                     realm, *args, **kwargs)
        return wrapper
    return view_decorator

def has_perm_or_basicauth(perm, realm = ""):

    def view_decorator(func):
        def wrapper(request, *args, **kwargs):
            return view_or_basicauth(func, request,
                                     lambda u: u.has_perm(perm),
                                     realm, *args, **kwargs)
        return wrapper
    return view_decorator

@login_required()
def inventory_dashboard_01(request):

    device_os_count = list()
    list_device_os = list(DeviceOS.objects.values_list('device_os', flat=True))
    for obj in list_device_os:
        count = DeviceBasicInfo.objects.filter(device_os__device_os=obj).count()
        device_os_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': device_os_count})

@login_required()
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

@login_required()
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
    list_location = list(DeviceLocation.objects.values_list('device_location', flat=True))
    for obj in list_location:
        point_01 = DeviceConfiguration.objects.filter(device_config_standardized=False, device_ip__device_location__device_location=obj).count()
        point_02 = DeviceConfiguration.objects.filter(device_monitored=False, device_ip__device_location__device_location=obj).count()
        point_03 = DeviceConfiguration.objects.filter(device_backup_config=False, device_ip__device_location__device_location=obj).count()
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

@login_required()
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

@login_required()
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
  
@login_required()  
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

@login_required()
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

@logged_in_or_basicauth()
def get_list_device(request):
    if request.method == 'GET':
        if request.GET.get('device_os') is not None and request.GET.get('device_category') is not None:
            device_os = request.GET['device_os']
            device_category = request.GET['device_category']
            datalist = list()
            queryset = DeviceBasicInfo.objects.filter(device_os__device_os=device_os, device_category__device_category=device_category)
            if len(queryset) > 0:
                for item in queryset:
                    datalist.append({
                        'device_ip': item.device_ip,
                        'device_name': item.device_name
                    })
            return JsonResponse({'datalist': datalist}, status=200)
        else:
            return JsonResponse({'error_message': 'missing request parameter'}, status=401)
        
