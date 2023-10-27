from django.shortcuts import render
from django.shortcuts import redirect
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


class IpRegoinCreateView(CreateView):
    model = IpRegoin
    form_class = IpRegoinForm
    template_name = "create_ip_regoin.html"
    success_url = '/ipplan/create-ip-regoin'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class IpLocationCreateView(CreateView):
    model = IpLocation
    form_class = IpLocationForm
    template_name = "create_ip_location.html"
    success_url = '/ipplan/create-ip-location'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class IpSubnetCreateView(CreateView):
    model = IpSubnet
    form_class = IpSubnetForm
    template_name = "create_ip_subnet.html"
    success_url = '/ipplan/list-ip-subnet'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class IpSubnetListView(ListView):
    model = IpSubnet
    context_object_name = 'subnets'
    template_name = "list_ip_subnet.html"


def request_ip_form(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'POST':
        form = RequestIpAddressForm(request.POST)
        if form.is_valid():
            subnet = form.cleaned_data.get('subnet')
            count = form.cleaned_data.get('count')
            description = form.cleaned_data.get('description')
            used_ips = IpAddressModel.objects.filter(subnet__subnet=subnet).values_list('ip_address', flat=True)
            list_ips = get_available_ips(subnet=subnet, used_ips=used_ips, count=count)
            return render(request, template_name='request_ip_result.html', context={'list_ips': list_ips, 'subnet': subnet, 'description': description})
        else:
            return render(request, template_name='request_ip.html', context={'form': form})
    else:
        form = RequestIpAddressForm()
    return render(request, template_name='request_ip.html', context={'form': form})

    
def dashboard(request):
    return render(request, template_name='dashboard.html')