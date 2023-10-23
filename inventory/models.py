from django.db import models

# Create your models here.

class DeviceLocation(models.Model):
    device_location = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_location
    
class DeviceType(models.Model):
    device_type = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_type
    
class DeviceCategory(models.Model):
    device_category = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_category
    
class DeviceVendor(models.Model):
    device_vendor = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_vendor
    
class DeviceModel(models.Model):
    device_name = models.CharField(max_length=1000)
    device_ip = models.GenericIPAddressField(unique=True)
    device_location = models.ForeignKey('DeviceLocation', on_delete=models.CASCADE)
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    device_category = models.ForeignKey('DeviceCategory', on_delete=models.CASCADE)
    device_vendor = models.ForeignKey('DeviceVendor', on_delete=models.CASCADE)
    device_description = models.CharField(max_length=1000)
    device_creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_ip

