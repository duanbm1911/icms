from django.shortcuts import render
from cm.models import *
from cm.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

# Create your views here.


def create_task(request):
    return render(request, template_name='create_task.html')


class CheckpointPolicyCreateView(CreateView):
    model = CheckpointPolicy
    form_class = CheckpointPolicyForm
    template_name = "create_policy.html"
    success_url = '/cm/objects/create-policy'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)
    
class CheckpointSiteCreateView(CreateView):
    model = CheckpointSite
    form_class = CheckpointSiteForm
    template_name = "create_site.html"
    success_url = '/cm/objects/create-site'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_created = str(self.request.user)
        messages.add_message(self.request, constants.SUCCESS, 'Create success')
        return super().form_valid(form)