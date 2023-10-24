from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.http import JsonResponse
from ipplan.models import *
from ipplan.forms import *

# Create your views here.


class IpLocationCreateView(CreateView):
    model = IpLocation
    form_class = IpLocationForm
    template_name = "create_ip_location.html"
    success_url = '/ipplan/create-ip-location'

    def form_valid(self, form):
        form.instance.user_created = self.request.user
        return super().form_valid(form)

class IpProjectCreateView(CreateView):
    model = IpProject
    form_class = IpProjectForm
    template_name = "create_ip_project.html"
    success_url = '/ipplan/create-ip-project'

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
