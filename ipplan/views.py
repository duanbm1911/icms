from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from ipplan.models import *
from ipplan.forms import *

# Create your views here.


class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = "create_region.html"
    success_url = '/ipplan/create-region'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "create_location.html"
    success_url = '/ipplan/create-location'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class SubnetCreateView(CreateView):
    model = Subnet
    form_class = SubnetForm
    template_name = "create_subnet.html"
    success_url = '/ipplan/list-subnet'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class SubnetListView(ListView):
    model = Subnet
    context_object_name = 'subnets'
    template_name = "list_subnet.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
@login_required()
def request_ip_form(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'POST':
        form = RequestIpAddressForm(request.POST)
        if form.is_valid():
            subnet = form.cleaned_data.get('subnet')
            count = form.cleaned_data.get('count')
            status = form.cleaned_data.get('status')
            description = form.cleaned_data.get('description')
            used_ips = IpAddressModel.objects.filter(subnet__subnet=subnet).values_list('ip_address', flat=True)
            list_ips = get_available_ips(subnet=subnet, used_ips=used_ips, count=count)
            for ip in list_ips:
                model = IpAddressModel.objects.create(
                    ip_address = ip,
                    subnet = subnet,
                    status = status,
                    description = description,
                    user_created = request.user
                )
                model.save
            return render(request, template_name='request_ip_result.html', context={'list_ips': list_ips, 'subnet': subnet, 'status': status})
        else:
            return render(request, template_name='request_ip.html', context={'form': form})
    else:
        form = RequestIpAddressForm()
    return render(request, template_name='request_ip.html', context={'form': form})

@login_required()
def dashboard(request):
    return render(request, template_name='dashboard.html')

@login_required()
def list_ip(request, pk):
    list_ip = IpAddressModel.objects.filter(subnet__id=pk)
    return render(request, template_name='list_ip.html', context={'list_ip': list_ip})


class IpAddressModelDeleteView(DeleteView):
    model = IpAddressModel
    template_name = 'list_ip.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        return IpAddressModel.objects.get(pk=self.kwargs["id"])

    def get_success_url(self):
        pk = self.kwargs["pk"]
        pk1 = self.kwargs['id']
        return reverse("list-ip", kwargs={"pk": pk})


class IpAddressModelUpdateView(UpdateView):
    model = IpAddressModel
    form_class = IpAddressModelUpdatelForm
    template_name = "update_ip.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        return IpAddressModel.objects.get(pk=self.kwargs["id"])

    def get_success_url(self):
        pk = self.kwargs["pk"]
        pk1 = self.kwargs['id']
        return reverse("list-ip", kwargs={"pk": pk})


class SubnetUpdateView(UpdateView):
    model = Subnet
    form_class = SubnetUpdateForm
    template_name = "update_subnet.html"
    success_url = '/ipplan/list-subnet'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class IpAddressModelDetailView(DetailView):
    model = IpAddressModel
    form_class = IpAddressModelForm
    template_name = "detail_ip.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        return IpAddressModel.objects.get(pk=self.kwargs["id"])


class SubnetDeleteView(DeleteView):
    model = Subnet
    template_name = "list-subnet.html"
    success_url = '/ipplan/list-subnet'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

