from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from inventory.models import *
from inventory.forms import *
# Create your views here.

class DeviceModelCreateView(CreateView):
    model = DeviceModel
    form_class = DeviceForm
    template_name = "create_device.html"
    success_url = '/inventory/list-device'
    
    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceLocationCreateView(CreateView):
    model = DeviceLocation
    form_class = DeviceLocationForm
    template_name = "create_device_location.html"
    success_url = 'create-device-location'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceTypeCreateView(CreateView):
    model = DeviceType
    form_class = DeviceTypeForm
    template_name = "create_device_type.html"
    success_url = 'create-device-type'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceCategoryCreateView(CreateView):
    model = DeviceCategory
    form_class = DeviceCategoryForm
    template_name = "create_device_category.html"
    success_url = 'create-device-category'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceVendorCreateView(CreateView):
    model = DeviceVendor
    form_class = DeviceVendorForm
    template_name = "create_device_vendor.html"
    success_url = 'create-device-vendor'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceModelListView(ListView):
    model = DeviceModel
    context_object_name = 'devices'
    template_name = "list_device.html"

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceModelUpdateView(UpdateView):
    model = DeviceModel
    form_class = DeviceForm
    template_name = "update_device.html"
    success_url = '/inventory/list-device'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class DeviceModelDeleteView(DeleteView):
    model = DeviceModel
    success_url = '/inventory/list-device'


class DeviceModelDetailView(DetailView):
    model = DeviceModel
    template_name = "detail_device.html"


def create_multiple_device(request):
    if request.method == 'POST' and request.FILES.get('upload-file'):
        uploaded_file = request.FILES['upload-file']
        print(uploaded_file.read().decode())
    return render(request, 'create_multiple_device.html')


def device_dashboard(request):
    return render(request, template_name='device_dashboard.html')
