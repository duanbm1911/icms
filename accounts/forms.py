from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_active', 'password1','password2'] 