from django.views.decorators.csrf import csrf_exempt
from src.cm.checkpoint.func import check_access_rule_input
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from inventory.models import *
from ipplan.models import *
from cm.models import *
import datetime
import base64
import json

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
        count = Device.objects.filter(device_os__device_os=obj).count()
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
        count = Device.objects.filter(device_vendor__device_vendor=obj).count()
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
    # color = lambda: random.randint(0,255)
    for data_point in list_data_point:
        chart_data.append({
            "type": "line",
            "showInLegend": "true",
            "name": data_point['desc'],
            "markerSize": 0,
            "markerType": "square",
            # "color": '#%02X%02X%02X' % (color(),color(),color()),
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
        count = Device.objects.filter(device_type__device_type=obj).count()
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
        count = Device.objects.filter(device_location__device_location=obj).count()
        location_count.append({
            'label': str(obj),
            'y': count
        })
    return JsonResponse({'data': location_count})


@login_required()
def inventory_dashboard_06(request):
    """
    This dashboard will be display count of incorrect firmware by device type
    """
    list_device_firmware = Device.objects.all().values_list('device_name', 'device_ip', 'device_type__device_type', 'device_firmware')
    list_firmware = DeviceFirmware.objects.all().values_list('device_type__device_type', 'firmware')
    list_device_type = DeviceType.objects.all().values_list('device_type', flat=True)
    datalist01 = list()
    datalist02 = list()
    for item in list_device_firmware:
        device_type = item[2]
        device_firmware = item[3]
        if device_firmware is not None:
            checklist = [i for i in list_firmware if i == (device_type, device_firmware)]
            if not checklist:
                datalist01.append(device_type)
    for item in list_device_type:
        count = datalist01.count(item)
        datalist02.append({
            'label': str(item),
            'y': count
        })
    return JsonResponse({'data': datalist02})

@login_required()
def inventory_dashboard_07(request):
    data_point_01 = list()
    data_point_02 = list()
    data_point_03 = list()
    data_point_04 = list()
    list_data_point = [
    {
        "name": data_point_01,
        "desc": "End MA"
    },
    {
        "name": data_point_02,
        "desc": "End License"
    },
    {
        "name": data_point_03,
        "desc": "End HW SP"
    },
    {
        "name": data_point_04,
        "desc": "End SW SP"
    }
    ]
    datepoint01 = datetime.date.today()
    datepoint02 = datetime.date.today() + datetime.timedelta(days=180)
    list_device_type = DeviceType.objects.all().values_list('device_type', flat=True)
    chart_data = list()
    for device_type in list_device_type:
        obj = DeviceType.objects.get(device_type=device_type)
        point_01 = DeviceManagement.objects.filter(device_ip__device_type=obj, end_ma_date__gte=datepoint01, end_ma_date__lte=datepoint02).count()
        point_02 = DeviceManagement.objects.filter(device_ip__device_type=obj, end_license_date__gte=datepoint01, end_license_date__lte=datepoint02).count()
        point_03 = DeviceManagement.objects.filter(device_ip__device_type=obj, end_sw_support_date__gte=datepoint01, end_sw_support_date__lte=datepoint02).count()
        point_04 = DeviceManagement.objects.filter(device_ip__device_type=obj, end_hw_support_date__gte=datepoint01, end_hw_support_date__lte=datepoint02).count()
        data_point_01.append({
            'label': device_type,
            'y': point_01
        })
        data_point_02.append({
            'label': device_type,
            'y': point_02
        })
        data_point_03.append({
            'label': device_type,
            'y': point_03
        })
        data_point_04.append({
            'label': device_type,
            'y': point_04
        })
    list_data_point = [{
        "name": data_point_01,
        "desc": "End MA"
    },
    {
        "name": data_point_02,
        "desc": "End License"
    },
    {
        "name": data_point_03,
        "desc": "End HW SP"
    },
    {
        "name": data_point_04,
        "desc": "End SW SP"
    }]
    for data_point in list_data_point:
        chart_data.append({
            "type": "line",
            "showInLegend": "true",
            "name": data_point['desc'],
            "markerSize": 0,
            "markerType": "square",
            "dataPoints": data_point['name']
        })
    return JsonResponse({'data': chart_data})
  
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
        datalist = list()
        queryset = Device.objects.all()
        if len(queryset) > 0:
            for item in queryset:
                datalist.append({
                    'device_ip': item.device_ip,
                    'device_name': item.device_name,
                    'device_os': item.device_os.device_os,
                    'device_category': item.device_category.device_category,
                    'device_vendor': item.device_vendor.device_vendor
                })
        return JsonResponse({'datalist': datalist}, status=200)
    else:
        return JsonResponse({'error_message': 'method not allowed'}, status=405)
        
@csrf_exempt
@logged_in_or_basicauth()
def update_device_check_config(request):
    if request.method == 'POST':
        datalist01 = request.POST.getlist('datalist01')
        datalist02 = request.POST.getlist('datalist02')
        if datalist01:
            for device_ip in datalist01:
                check_device_exists = Device.objects.filter(device_ip=device_ip).count()
                if check_device_exists > 0:
                    obj = Device.objects.get(device_ip=device_ip)
                    DeviceConfiguration.objects.update_or_create(
                        device_ip=obj,
                        defaults={
                            'device_config_standardized': True
                        })
        if datalist02:
            for device_ip in datalist02:
                check_device_exists = Device.objects.filter(device_ip=device_ip).count()
                if check_device_exists > 0:
                    obj = Device.objects.get(device_ip=device_ip)
                    DeviceConfiguration.objects.update_or_create(
                        device_ip=obj,
                        defaults={
                            'device_config_standardized': False
                        })
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'error_message': 'method not allowed'}, status=405)
    
@csrf_exempt
@logged_in_or_basicauth()
def update_device_check_monitor(request):
    if request.method == 'POST':
        datalist01 = request.POST.getlist('datalist01')
        datalist02 = request.POST.getlist('datalist02')
        if datalist01:
            for device_ip in datalist01:
                check_device_exists = Device.objects.filter(device_ip=device_ip).count()
                if check_device_exists > 0:
                    obj = Device.objects.get(device_ip=device_ip)
                    DeviceConfiguration.objects.update_or_create(
                        device_ip=obj,
                        defaults={
                            'device_monitored': True
                        })
        if datalist02:
            for device_ip in datalist02:
                check_device_exists = Device.objects.filter(device_ip=device_ip).count()
                if check_device_exists > 0:
                    obj = Device.objects.get(device_ip=device_ip)
                    DeviceConfiguration.objects.update_or_create(
                        device_ip=obj,
                        defaults={
                            'device_monitored': False
                        })
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'error_message': 'method not allowed'}, status=405)
    
@csrf_exempt
@logged_in_or_basicauth()
def update_device_firmware(request):
    if request.method == 'POST':
        dataset = request.POST.dict()
        for device_ip, firmware in dataset.items():
            Device.objects.update_or_create(
                device_ip=device_ip,
                defaults={
                    'device_firmware': firmware
                })
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'error_message': 'method not allowed'}, status=405)

@csrf_exempt
@logged_in_or_basicauth()
def update_device_interface(request):
    if request.method == 'POST':
        dataset = json.loads(request.body.decode('utf-8'))
        for device_ip, data in dataset.items():
            checklist = Device.objects.filter(device_ip=device_ip).count()
            if checklist > 0:
                obj = Device.objects.get(device_ip=device_ip)
                DeviceInterface.objects.update_or_create(
                    device_ip=obj,
                    defaults={
                        'list_interface_name': data['list_interface_name'],
                        'list_interface_desc': data['list_interface_desc'],
                        'list_interface_speed': data['list_interface_speed'],
                        'list_interface_type': data['list_interface_type'],
                        'list_interface_state': data['list_interface_state']
                    })
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'error_message': 'method not allowed'}, status=405)


def device_report():
    queryset_01 = DeviceManagement.objects.all()
    count_01 = queryset_01.count()
    countlist = list()
    list_device_vendor = DeviceVendor.objects.filter().values_list('device_vendor', flat=True)
    for device_vendor in list_device_vendor:
        count = DeviceManagement.objects.filter(device_ip__device_vendor__device_vendor=device_vendor).count()
        countlist.append({
            'device_vendor': device_vendor,
            'count': count
        })
    datalist = {
        'device_count': count_01,
        'count_by_vendor': countlist
    }
    return datalist

def device_management_report():
    datalist = list()
    datepoint01 = datetime.date.today()
    datepoint02 = datetime.date.today() + datetime.timedelta(days=180)
    count_01 = DeviceManagement.objects.filter(end_ma_date__gte=datepoint01, end_ma_date__lte=datepoint02).count()
    count_02 = DeviceManagement.objects.filter(end_license_date__gte=datepoint01, end_license_date__lte=datepoint02).count()
    count_03 = DeviceManagement.objects.filter(end_sw_support_date__gte=datepoint01, end_sw_support_date__lte=datepoint02).count()
    count_04 = DeviceManagement.objects.filter(end_hw_support_date__gte=datepoint01, end_hw_support_date__lte=datepoint02).count()
    datalist = {
        'list_end_ma': count_01,
        'list_end_license': count_02,
        'list_end_sw_sp': count_03,
        'list_end_hw_sp': count_04
    }
    return datalist

def device_configuration_report():
    datalist = list()
    device_config_status = list()
    device_monitor_status = list()
    device_backup_status = list()
    list_device_os = list(DeviceOS.objects.values_list('device_os', flat=True))
    for device_os in list_device_os:
        count_01 = DeviceConfiguration.objects.filter(device_config_standardized=False, device_ip__device_os__device_os=device_os).count()
        count_02 = DeviceConfiguration.objects.filter(device_monitored=False, device_ip__device_os__device_os=device_os).count()
        count_03 = DeviceConfiguration.objects.filter(device_backup_config=False, device_ip__device_os__device_os=device_os).count()
        if count_01 != 0:
            device_config_status.append({
                'device_os': device_os,
                'count': count_01
            })
        if count_02 != 0:
            device_monitor_status.append({
                'device_os': device_os,
                'count': count_02
            })
        if count_03 != 0:
            device_backup_status.append({
                'device_os': device_os,
                'count': count_03
            })
    datalist = {
        'device_config_status': device_config_status,
        'device_monitor_status': device_monitor_status,
        'device_backup_status': device_backup_status
    }
    return datalist

def device_firmmware_report():
    list_device_firmware = Device.objects.all().values_list('device_name', 'device_ip', 'device_type__device_type', 'device_firmware')
    list_firmware = DeviceFirmware.objects.all().values_list('device_type__device_type', 'firmware')
    list_device_type = DeviceType.objects.all().values_list('device_type', flat=True)
    datalist01 = list()
    datalist02 = list()
    for item in list_device_firmware:
        device_type = item[2]
        device_firmware = item[3]
        if device_firmware is not None:
            checklist = [i for i in list_firmware if i == (device_type, device_firmware)]
            if not checklist:
                datalist01.append(device_type)
    for device_type in list_device_type:
        count = datalist01.count(device_type)
        if count != 0:
            datalist02.append({
                'device_type': device_type,
                'count': count
            })
    return datalist02


@logged_in_or_basicauth()
def inventory_report(request):
    device = device_report()
    device_management = device_management_report()
    device_configuration = device_configuration_report()
    device_firmmware = device_firmmware_report()
    data = {
        'device': device,
        'device_management': device_management,
        'device_configuration': device_configuration,
        'device_firmmware': device_firmmware
    }
    return JsonResponse({'data': data})

@login_required()
@csrf_exempt
def cm_checkpoint_create_task(request):
    try:
        if request.user.groups.filter(name='ADMIN').exists():
            if request.method == 'POST':
                list_obj = list(request.POST)
                list_error_message = str()
                list_task = list()
                status = 'Processing'
                user_created = request.user
                for obj in list_obj:
                    index = list_obj.index(obj)
                    data = request.POST.getlist(obj)
                    error_message = check_access_rule_input(data, index)
                    if not error_message:
                        policy = data[0]
                        description = data[1]
                        source = [i.replace(' ', '').replace('\r', '') for i in data[2].split('\n')]
                        destination = [i.replace(' ', '').replace('\r', '') for i in data[3].split('\n')]
                        protocol = [i.replace(' ', '').replace('\r', '') for i in data[4].split('\n')]
                        schedule = data[5]
                        list_task.append([
                            policy, 
                            description, 
                            json.dumps(source), 
                            json.dumps(destination),
                            json.dumps(protocol),
                            schedule,
                            status,
                            user_created
                            ])
                    else:
                        list_error_message += error_message + '\n'
                if list_error_message:
                    return JsonResponse({'status': 'failed', 'message': list_error_message}, status=200)
                else:
                    for item in list_task:
                        model = CheckpointTask(
                            policy=CheckpointPolicy.objects.get(policy=item[0]),
                            description=item[1],
                            source=item[2],
                            destination=item[3],
                            protocol=item[4],
                            schedule=item[5],
                            status=item[6],
                            user_created=item[7],
                        )
                        model.save()
                    return JsonResponse({'status': 'success', 'message': 'Create task success'}, status=200)
            else:
                return JsonResponse({'status': 'failed', 'message': 'Request method is not allowed'}, status=405)
        else:
            return JsonResponse({'erorr': 'forbidden'}, status=403)
    except:
        return JsonResponse({'status': 'failed', 'message': 'Exception error'}, status=500)

@login_required()
def cm_checkpoint_get_list_policy(request):
    if request.user.groups.filter(name='ADMIN').exists():
        if request.method == 'GET':
            datalist = CheckpointPolicy.objects.all().values_list('policy', flat=True)
            return JsonResponse({'data': list(datalist)}, status=200)
        else:
            return JsonResponse({'erorr': 'Method is not allowed'}, status=405)
    else:
        return JsonResponse({'erorr': 'forbidden'}, status=403)

@logged_in_or_basicauth()
def cm_checkpoint_get_list_task(request):
    if request.user.groups.filter(name='ADMIN').exists():
        if request.method == 'GET':
            datalist = CheckpointTask.objects.filter(status='Processing').values_list('id', 'policy__site_name__site_name', 'policy__policy', 'description', 'source', 'destination', 'protocol', 'schedule')
            datalist = [list(i) for i in datalist]
            if datalist != []:
                for item in datalist:
                    item[4] = json.loads(item[4])
                    item[5] = json.loads(item[5])
                    item[6] = json.loads(item[6])
            return JsonResponse({'datalist': list(datalist)},  status=200)
        else:
            return JsonResponse({'erorr': 'Method is not allowed'}, status=405)
    else:
        return JsonResponse({'erorr': 'forbidden'}, status=403)

@csrf_exempt
@logged_in_or_basicauth()
def cm_checkpoint_update_task_status(request):
    if request.user.groups.filter(name='ADMIN').exists():
        if request.method == 'POST':
            dataset = request.POST.dict()
            policy_id = dataset['policy_id']
            status = dataset['status']
            message = dataset['message']
            model = CheckpointTask.objects.filter(id=policy_id)
            model.update(
                status=status,
                message=message
            )
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'erorr': 'Method is not allowed'}, status=405)
    else:
        return JsonResponse({'erorr': 'forbidden'}, status=403)