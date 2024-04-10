from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def redirect_home_url(request):
    return redirect('/inventory/device-dashboard')


def error_404(request, exception):
   return render(request, template_name='404.html')