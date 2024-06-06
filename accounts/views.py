from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.messages import constants
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from accounts.models import *
from accounts.forms import *
import pyotp
import qrcode
import time

# Create your views here.


def get_client_ip(request):
    client_ip = str()
    if request.META.get('HTTP_CLIENT_IP') is not None:
        client_ip = request.META.get('HTTP_CLIENT_IP')
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip

def logout(request):
    auth_logout(request)
    return redirect('/accounts/login')

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = ValidatingPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ValidatingPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        otp = request.POST.get("otp")
        client_ip = get_client_ip(request)
        user = authenticate(username=username, password=password)
        obj = ClientLoginFailedSession.objects.filter(client_ip=client_ip, username=username)
        login_failed_count = 0
        if obj.count() > 0:
            login_failed_count = obj[0].failed_count
        if login_failed_count <= 5:
            retries_login_count = 5 - login_failed_count
            if user is not None:
                verify_otp_result = verify_otp(user, otp)
                if verify_otp_result:
                    auth_login(request, user)
                    login_failed = ClientLoginFailedSession.objects.filter(client_ip=client_ip, username=username)
                    login_failed.delete()
                    return redirect('/')
            else:
                if login_failed_count <= 5:
                    obj = ClientLoginFailedSession.objects.get(client_ip=client_ip, username=username)
                    failed_count = obj.failed_count
                    obj.failed_count = failed_count + 1
                    obj.save()
            messages.add_message(request, constants.ERROR, f'Login failed, The account will be locked after {retries_login_count} failed attempts ')
        else:
            messages.add_message(request, constants.ERROR, f'Account: {username} has been locked, please contact with Administrator')
    return render(request, "registration/login.html")
    
def verify_otp(user, otp):
    try:
        obj = User.objects.get(username=user)
        model = UserOTP.objects.get(user=obj)
        otp_key = model.otp_key
        totp = pyotp.TOTP(otp_key)
        result = totp.verify(otp)
        return result
    except:
        return False
    
def register(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            form = RegisterForm()
        else:
            form = RegisterForm(request.POST) 
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Register user success')
                return redirect('/accounts/list-users')
        return render(request, 'registration/register.html', { 'form': form})
    else:
        return render(request, template_name='403.html')
    
class UserListView(ListView):
    model = User
    context_object_name = 'objects'
    template_name = "list_user.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            return render(self.request, template_name='403.html')
        return super().dispatch(*args, **kwargs)