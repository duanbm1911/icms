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




def logout(request):
    auth_logout(request)
    return redirect('/accounts/login')

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        otp = request.POST.get("otp")
        user = authenticate(username=username, password=password)
        if user is not None:
            verify_otp_result = verify_otp(user, otp)
            print(verify_otp_result)
            if verify_otp_result:
                auth_login(request, user)
                return redirect('/')
        messages.add_message(request, constants.ERROR, 'Login failed')
    return render(request, "registration/login.html")
    
def verify_otp(user, otp):
    # try:
        obj = User.objects.get(username=user)
        print(obj)
        model = UserOTP.objects.get(user=obj)
        print(model.key)
        otp_key = model.otp_key
        totp = pyotp.TOTP(otp_key)
        print(totp)
        result = totp.verify(otp)
        return result
    # except:
    #     return False
    
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