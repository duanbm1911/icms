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
from accounts.models import *
import pyotp
import qrcode

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
            if verify_otp_result:
                auth_login(request, user)
                return redirect('/')
        messages.add_message(request, constants.ERROR, 'Login failed')
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
    
    