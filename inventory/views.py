from django.db.models import ProtectedError
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from inventory.models import *
from inventory.forms import *
import openpyxl
# Create your views here.

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


class DeviceBasicInfoCreateView(CreateView):
    model = DeviceBasicInfo
    form_class = DeviceBasicInfoForm
    template_name = "create_device.html"
    success_url = '/inventory/list-device/device-basic-info'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceLocationCreateView(CreateView):
    model = DeviceLocation
    form_class = DeviceLocationForm
    template_name = "create_device_location.html"
    success_url = '/inventory/list-device-location'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceLocationUpdateView(UpdateView):
    model = DeviceLocation
    form_class = DeviceLocationForm
    template_name = "update_device_location.html"
    success_url = '/inventory/list-device-location'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class DeviceLocationDeleteView(DeleteView):
    model = DeviceLocation
    template_name = 'list_device_location.html'
    success_url = '/inventory/list-device-location'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceLocationListView(ListView):
    model = DeviceLocation
    context_object_name = 'objects'
    template_name = "list_device_location.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceTypeCreateView(CreateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = "create_device_type.html"
    success_url = '/inventory/list-device-type'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceTypeListView(ListView):
    model = DeviceType
    context_object_name = 'objects'
    template_name = "list_device_type.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceTypeUpdateView(UpdateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = "update_device_type.html"
    success_url = '/inventory/list-device-type'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class DeviceTypeDeleteView(DeleteView):
    model = DeviceType
    template_name = 'list_device_type.html'
    success_url = '/inventory/list-device-type'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceCategoryCreateView(CreateView):
    model = DeviceCategory
    form_class = DeviceCategoryForm
    template_name = "create_device_category.html"
    success_url = 'list-device-category'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceCategoryListView(ListView):
    model = DeviceCategory
    context_object_name = 'objects'
    template_name = "list_device_category.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceCategoryUpdateView(UpdateView):
    model = DeviceCategory
    form_class = DeviceCategoryForm
    template_name = "update_device_category.html"
    success_url = '/inventory/list-device-category'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class DeviceCategoryDeleteView(DeleteView):
    model = DeviceCategory
    template_name = 'list_device_category.html'
    success_url = '/inventory/list-device-category'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceVendorCreateView(CreateView):
    model = DeviceVendor
    form_class = DeviceVendorForm
    template_name = "create_device_vendor.html"
    success_url = '/inventory/list-device-vendor'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceVendorListView(ListView):
    model = DeviceVendor
    context_object_name = 'objects'
    template_name = "list_device_vendor.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceVendorUpdateView(UpdateView):
    model = DeviceVendor
    form_class = DeviceVendorForm
    template_name = "update_device_vendor.html"
    success_url = '/inventory/list-device-vendor'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class DeviceVendorDeleteView(DeleteView):
    model = DeviceVendor
    template_name = 'list_device_vendor.html'
    success_url = '/inventory/list-device-vendor'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceBasicInfoListView(ListView):
    model = DeviceBasicInfo
    context_object_name = 'devices'
    template_name = "list_device_basic_info.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceBasicInfoUpdateView(UpdateView):
    model = DeviceBasicInfo
    form_class = DeviceBasicInfoForm
    template_name = "update_device.html"
    success_url = '/inventory/list-device/device-basic-info'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class DeviceBasicInfoDeleteView(DeleteView):
    model = DeviceBasicInfo
    template_name = 'list_device_basic_info.html'
    success_url = '/inventory/list-device/device-basic-info'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceBasicInfoDetailView(DetailView):
    model = DeviceBasicInfo
    template_name = "detail_device_basic_info.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
@login_required()
def create_multiple_device(request):
    try:
        if request.method == 'POST' and request.FILES.get('upload-file'):
            uploaded_file = request.FILES['upload-file']
            wb = openpyxl.load_workbook(uploaded_file)
            sheets = wb.sheetnames
            worksheet_01 = wb["Device_basic_info"]
            worksheet_02 = wb["Device_management"]
            worksheet_03 = wb["Device_topology"]
            excel_data = list()
            for item in worksheet_01.iter_rows(min_row=2, values_only=True):
                item = ["" if i is None else i for i in item]
                obj_count = DeviceBasicInfo.objects.filter(device_ip=item[1]).count()
                if obj_count == 0:
                    obj_count_01 = DeviceLocation.objects.filter(device_location=item[2]).count()
                    obj_count_02 = DeviceType.objects.filter(device_type=item[3]).count()
                    obj_count_03 = DeviceCategory.objects.filter(device_category=item[4]).count()
                    obj_count_04 = DeviceVendor.objects.filter(device_vendor=item[5]).count()
                    obj_count_05 = DeviceOS.objects.filter(device_os=item[6]).count()
                    if obj_count_01 == 0:
                        model_01 = DeviceLocation(device_location=item[2])
                        model_01.save()
                    if obj_count_02 == 0:
                        model_02 = DeviceType(device_type=item[3])
                        model_02.save()
                    if obj_count_03 == 0:
                        model_03 = DeviceCategory(device_category=item[4])
                        model_03.save()
                    if obj_count_04 == 0:
                        model_04 = DeviceVendor(device_vendor=item[5])
                        model_04.save()
                    if obj_count_05 == 0:
                        model_05 = DeviceOS(device_os=item[6])
                        model_05.save()
                    model = DeviceBasicInfo(
                        device_name=item[0],
                        device_ip=item[1],
                        device_location=DeviceLocation.objects.get(device_location=item[2]),
                        device_type=DeviceType.objects.get(device_type=item[3]),
                        device_category=DeviceCategory.objects.get(device_category=item[4]),
                        device_vendor=DeviceVendor.objects.get(device_vendor=item[5]),
                        device_os=DeviceOS.objects.get(device_os=item[6]),
                        device_stack=item[7],
                        device_description=item[8],
                        user_created=request.user
                    )
                    model.save()
            for item in worksheet_02.iter_rows(min_row=2, values_only=True):
                if item[0] is not None and item[1] is not None:
                    obj_count = DeviceBasicInfo.objects.filter(device_ip=item[1]).count()
                    if obj_count == 1:
                        device_is_stack = DeviceBasicInfo.objects.get(device_ip=item[1]).device_stack
                        obj_count_01 = DeviceManagement.objects.filter(device_ip=DeviceBasicInfo.objects.get(device_ip=item[1])).count()
                        obj_count_02 = DeviceManagement.objects.filter(device_serial_number=item[2]).count()
                        if obj_count_01 == 0 or (obj_count_01 == 1 and device_is_stack == True):
                            if obj_count_02 == 0:
                                model = DeviceManagement(
                                    device_ip=DeviceBasicInfo.objects.get(device_ip=item[1]),
                                    device_serial_number=item[2],
                                    start_ma_date=item[3],
                                    end_ma_date=item[4],
                                    start_license_date=item[5],
                                    end_license_date=item[6],
                                    end_sw_support_date=item[7],
                                    end_hw_support_date=item[8],
                                    start_used_date=item[9],
                                    user_created=request.user
                                )
                                model.save()
            for item in worksheet_03.iter_rows(min_row=2, values_only=True):
                if item[0] is not None and item[1] is not None:
                    obj_count = DeviceBasicInfo.objects.filter(device_ip=item[1]).count()
                    if obj_count != 0:
                        device_is_stack = DeviceBasicInfo.objects.get(device_ip=item[1]).device_stack
                        obj_count_01 = DeviceTopology.objects.filter(device_ip=DeviceBasicInfo.objects.get(device_ip=item[1])).count()
                        if obj_count_01 == 0:
                            model = DeviceTopology(
                                device_ip=DeviceBasicInfo.objects.get(device_ip=item[1]),
                                device_rack_name=item[2],
                                device_rack_unit=item[3],
                                user_created=request.user
                            )
                            model.save()
                        elif obj_count_01 == 1 and device_is_stack == True:
                            obj = DeviceTopology.objects.get(device_ip=DeviceBasicInfo.objects.get(device_ip=item[1]))
                            rack_name = obj.device_rack_name
                            rack_unit = obj.device_rack_unit
                            if rack_name != item[2] or rack_unit != item[3]:
                                model = DeviceTopology(
                                    device_ip=DeviceBasicInfo.objects.get(device_ip=item[1]),
                                    device_rack_name=item[2],
                                    device_rack_unit=item[3],
                                    user_created=request.user
                                )
                                model.save()
            messages.add_message(request, constants.SUCCESS, 'Import devices success')
    except Exception as error:
        messages.add_message(request, constants.ERROR, f'An error occurred: {error}')
    return render(request, 'create_multiple_device.html')

@login_required()
def device_dashboard(request):
    return render(request, template_name='device_dashboard.html')

class DeviceManagementListView(ListView):
    model = DeviceManagement
    form_class = DeviceManagementForm
    context_object_name = 'devices'
    template_name = "list_device_management.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceManagementCreateView(CreateView):
    model = DeviceManagement
    form_class = DeviceManagementForm
    template_name = "create_device_management.html"
    success_url = '/inventory/list-device/device-management'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)
    
class DeviceManagementDeleteView(DeleteView):
    model = DeviceManagement
    template_name = 'list_device_basic_info.html'
    success_url = '/inventory/list-device/device-management'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class DeviceInterfaceListView(ListView):
    model = DeviceInterface
    form_class = DeviceInterfaceForm
    context_object_name = 'devices'
    template_name = "list_device_interface.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceTopologyListView(ListView):
    model = DeviceTopology
    form_class = DeviceTopologyForm
    context_object_name = 'devices'
    template_name = "list_device_topology.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceTopologyCreateView(CreateView):
    model = DeviceTopology
    form_class = DeviceTopologyForm
    template_name = "create_device_topology.html"
    success_url = '/inventory/list-device/device-topology'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class DeviceConfigurationListView(ListView):
    model = DeviceConfiguration
    form_class = DeviceConfigurationForm
    context_object_name = 'devices'
    template_name = "list_device_configuration.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceInterfaceDetailView(DetailView):
    model = DeviceInterface
    template_name = "detail_device_interface.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceManagementUpdateView(UpdateView):
    model = DeviceManagement
    form_class = DeviceManagementForm
    template_name = 'update_device_management.html'
    success_url = '/inventory/list-device/device-management'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)
    
class DeviceManagementDetailView(DetailView):
    model = DeviceManagement
    template_name = 'detail_device_management.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class DeviceTopologyUpdateView(UpdateView):
    model = DeviceTopology
    form_class = DeviceTopologyForm
    template_name = 'update_device_topology.html'
    success_url = '/inventory/list-device/device-topology'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)
    
class DeviceTopologyDetailView(DetailView):
    model = DeviceTopology
    template_name = 'detail_device_topology.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class DeviceTopologyDeleteView(DeleteView):
    model = DeviceTopology
    template_name = 'list_device_topology.html'
    success_url = '/inventory/list-device/device-topology'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)