from django.shortcuts import render
from django.db.models import ProtectedError
from django.http import HttpResponse
from cm.models import *
from cm.forms import *
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import TemplateView

# Create your views here.

class CheckpointRuleView(TemplateView):
    template_name = "checkpoint/create_rule.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

class CheckpointPolicyCreateView(CreateView):
    model = CheckpointPolicy
    form_class = CheckpointPolicyForm
    template_name = "checkpoint/create_policy.html"
    success_url = '/cm/checkpoint/objects/create-policy'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)
    
class CheckpointPolicyListView(ListView):
    model = CheckpointPolicy
    context_object_name = 'objects'
    template_name = "checkpoint/list_policy.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CheckpointPolicyUpdateView(UpdateView):
    model = CheckpointPolicy
    form_class = CheckpointPolicyForm
    template_name = "checkpoint/update_policy.html"
    success_url = '/cm/checkpoint/objects/list-policy'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class CheckpointPolicyDeleteView(DeleteView):
    model = CheckpointPolicy
    template_name = 'checkpoint/list_policy.html'
    success_url = '/cm/checkpoint/objects/list-policy'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)

class CheckpointSiteCreateView(CreateView):
    model = CheckpointSite
    form_class = CheckpointSiteForm
    template_name = "checkpoint/create_site.html"
    success_url = '/cm/checkpoint/objects/create-site'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)
    
class CheckpointSiteListView(ListView):
    model = CheckpointSite
    context_object_name = 'objects'
    template_name = "checkpoint/list_site.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CheckpointSiteUpdateView(UpdateView):
    model = CheckpointSite
    form_class = CheckpointSiteForm
    template_name = "checkpoint/update_site.html"
    success_url = '/cm/checkpoint/objects/list-site'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class CheckpointSiteDeleteView(DeleteView):
    model = CheckpointSite
    template_name = 'checkpoint/list_site.html'
    success_url = '/cm/checkpoint/objects/list-site'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)
    

class CheckpointRuleListView(ListView):
    model = CheckpointRule
    context_object_name = 'objects'
    template_name = "checkpoint/list_rule.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'list_rule_created': CheckpointRule.objects.filter(Q(status='Created') | Q(status='Install-Only')),
            'list_rule_process': CheckpointRule.objects.filter(status='Processing'),
            'list_rule_success': CheckpointRule.objects.filter(status='Success').order_by('-id'),
            'list_rule_failed': CheckpointRule.objects.filter(status='Failed'),
        }
        return context
    
class CheckpointRuleDeleteView(DeleteView):
    model = CheckpointRule
    template_name = 'checkpoint/list_site.html'
    success_url = '/cm/checkpoint/list-rule'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            messages.add_message(self.request, constants.SUCCESS, 'Delete success')
        except ProtectedError:
            messages.add_message(self.request, constants.ERROR, 'This object has been protected')
        except Exception as error:
            messages.add_message(self.request, constants.ERROR, error)
        return redirect(self.success_url)
    
class CheckpointRuleDetailView(DetailView):
    model = CheckpointRule
    template_name = "checkpoint/detail_rule.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    
class CheckpointRuleUpdateView(UpdateView):
    model = CheckpointRule
    form_class = CheckpointRuleForm
    template_name = "checkpoint/update_rule.html"
    success_url = '/cm/checkpoint/list-rule'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='checkpoint/403.html')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)
    

class F5DeviceCreateView(CreateView):
    model = F5Device
    form_class = F5DeviceForm
    template_name = "f5/create_device.html"
    success_url = '/cm/f5/list-device'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)

class F5DeviceUpdateView(UpdateView):
    model = F5Device
    form_class = F5DeviceForm
    template_name = "f5/update_device.html"
    success_url = '/cm/f5/list-device'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class F5DeviceDeleteView(DeleteView):
    model = F5Device
    template_name = 'f5/list_device.html'
    success_url = '/cm/f5/list-device'

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

# class F5DeviceListView(ListView):
#     model = F5Device
#     context_object_name = 'objects'
#     template_name = "f5/list_device.html"

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    

# class F5CreateVirtualServerUpdateView(UpdateView):
#     model = F5CreateVirtualServer
#     form_class = F5CreateVirtualServerForm
#     template_name = "f5/update_virtual_server.html"
#     success_url = '/cm/f5/list-virtual-server'

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.instance.user_created = str(self.request.user)
#         messages.add_message(self.request, constants.SUCCESS, 'Update success')
#         return super().form_valid(form)

# class F5CreateVirtualServerDeleteView(DeleteView):
#     model = F5CreateVirtualServer
#     template_name = 'f5/list_virtual_server.html'
#     success_url = '/cm/f5/list-virtual-server'

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         try:
#             super().post(request, *args, **kwargs)
#             messages.add_message(self.request, constants.SUCCESS, 'Delete success')
#         except ProtectedError:
#             messages.add_message(self.request, constants.ERROR, 'This object has been protected')
#         except Exception as error:
#             messages.add_message(self.request, constants.ERROR, error)
#         return redirect(self.success_url)

# class F5CreateVirtualServerListView(ListView):
#     model = F5CreateVirtualServer
#     context_object_name = 'objects'
#     template_name = "f5/list_virtual_server.html"

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    

# class F5CreateVirtualServerCreateView(CreateView):
#     model = F5CreateVirtualServer
#     form_class = F5CreateVirtualServerForm
#     template_name = "f5/create_virtual_server.html"
#     success_url = '/cm/f5/objects/list-virtual-server'

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.groups.filter(name='ADMIN').exists():
#             return render(request, template_name='f5/403.html')
#         return super().dispatch(request, *args, **kwargs)
    

class F5TemplateUpdateView(UpdateView):
    model = F5Template
    form_class = F5TemplateForm
    template_name = "f5/update_template.html"
    success_url = '/cm/f5/list-template'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class F5TemplateDeleteView(DeleteView):
    model = F5Template
    template_name = 'f5/list_template.html'
    success_url = '/cm/f5/list-template'

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

class F5TemplateListView(ListView):
    model = F5Template
    context_object_name = 'objects'
    template_name = "f5/list_template.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class F5TemplateCreateView(CreateView):
    model = F5Template
    form_class = F5TemplateForm
    template_name = "f5/create_template.html"
    success_url = '/cm/f5/list-template'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='ADMIN').exists():
            return render(request, template_name='f5/403.html')
        return super().dispatch(request, *args, **kwargs)
    
class F5TemplateDetailView(DetailView):
    model = F5Template
    template_name = "f5/detail_template.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)