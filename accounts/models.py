from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_key = models.CharField(max_length=500)
    qrcode_url = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.user)
    
    