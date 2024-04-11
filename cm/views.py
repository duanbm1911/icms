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
            'list_rule_created': CheckpointRule.objects.filter(Q(status='Created') | Q(status='ForceInstall')),
            'list_rule_process': CheckpointRule.objects.filter(status='Processing'),
            'list_rule_success': CheckpointRule.objects.filter(status='Success').order_by('-id')[:500],
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