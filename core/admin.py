from django.contrib import admin
from cm.models import *
from inventory.models import *
from ipplan.models import *
from django.contrib.auth.models import *
from accounts.models import *

# Register your models here.

from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "ICMS ADMINISTRATOR"
    
    
admin_site = MyAdminSite(name="ICMS_ADMIN")
admin_site.register(DeviceProvince)
admin_site.register(DeviceType)
admin_site.register(DeviceCategory)
admin_site.register(DeviceVendor)
admin_site.register(DeviceOS)
admin_site.register(Device)
admin_site.register(DeviceManagement)
admin_site.register(DeviceInterface)
admin_site.register(DeviceRackLayout)
admin_site.register(DeviceConfiguration)
admin_site.register(DeviceFirmware)
admin_site.register(DeviceBranch)
admin_site.register(DeviceTag)

admin_site.register(CheckpointRule)
admin_site.register(CheckpointSite)
admin_site.register(CheckpointPolicy)

admin_site.register(Region)
admin_site.register(Location)
admin_site.register(Subnet)
admin_site.register(IpStatus)
admin_site.register(IpAddressModel)

admin_site.register(User)
admin_site.register(Group)

admin_site.register(UserOTP)