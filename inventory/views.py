from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from inventory.models import *
from inventory.forms import *
# Create your views here.

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
        return super().form_valid(form)

class DeviceLocationCreateView(CreateView):
    model = DeviceLocation
    form_class = DeviceLocationForm
    template_name = "create_device_location.html"
    success_url = 'create-device-location'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        return super().form_valid(form)

class DeviceTypeCreateView(CreateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = "create_device_type.html"
    success_url = 'create-device-type'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        return super().form_valid(form)

class DeviceCategoryCreateView(CreateView):
    model = DeviceCategory
    form_class = DeviceCategoryForm
    template_name = "create_device_category.html"
    success_url = 'create-device-category'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        return super().form_valid(form)

class DeviceVendorCreateView(CreateView):
    model = DeviceVendor
    form_class = DeviceVendorForm
    template_name = "create_device_vendor.html"
    success_url = 'create-device-vendor'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        return super().form_valid(form)

class DeviceBasicInfoListView(ListView):
    model = DeviceBasicInfo
    context_object_name = 'devices'
    template_name = "list_device_basic_info.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        return super().form_valid(form)

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
        return super().form_valid(form)

class DeviceBasicInfoDeleteView(DeleteView):
    model = DeviceBasicInfo
    template_name = 'list_device.html'
    success_url = '/inventory/list-device'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DeviceBasicInfoDetailView(DetailView):
    model = DeviceBasicInfo
    template_name = "detail_device_basic_info.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
@login_required()
def create_multiple_device(request):
    if request.method == 'POST' and request.FILES.get('upload-file'):
        uploaded_file = request.FILES['upload-file']
        print(uploaded_file.read().decode())
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
        return super().form_valid(form)
    
class DeviceManagementDetailView(DetailView):
    model = DeviceManagement
    template_name = 'detail_device_management.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)