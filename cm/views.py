from django.shortcuts import render
from django.db.models import ProtectedError
from cm.models import *
from cm.forms import *
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

class CheckpointTaskView(TemplateView):
    template_name = "checkpoint/create_task.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CheckpointPolicyCreateView(CreateView):
    model = CheckpointPolicy
    form_class = CheckpointPolicyForm
    template_name = "checkpoint/create_policy.html"
    success_url = '/cm/checkpoint/objects/create-policy'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class CheckpointPolicyDeleteView(DeleteView):
    model = CheckpointPolicy
    template_name = 'checkpoint/list_policy.html'
    success_url = '/cm/checkpoint/objects/list-policy'

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

class CheckpointSiteCreateView(CreateView):
    model = CheckpointSite
    form_class = CheckpointSiteForm
    template_name = "checkpoint/create_site.html"
    success_url = '/cm/checkpoint/objects/create-site'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Update success')
        return super().form_valid(form)

class CheckpointSiteDeleteView(DeleteView):
    model = CheckpointSite
    template_name = 'checkpoint/list_site.html'
    success_url = '/cm/checkpoint/objects/list-site'

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
    

class CheckpointTaskListView(ListView):
    model = CheckpointTask
    context_object_name = 'objects'
    template_name = "checkpoint/list_task.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class CheckpointTaskDeleteView(DeleteView):
    model = CheckpointTask
    template_name = 'checkpoint/list_site.html'
    success_url = '/cm/checkpoint/list-task'

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
    
class CheckpointTaskDetailView(DetailView):
    model = CheckpointTask
    template_name = "checkpoint/detail_task.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)