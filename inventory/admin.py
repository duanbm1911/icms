from django.contrib import admin
from inventory.models import *

# Register your models here.

admin.site.register(DeviceLocation)
admin.site.register(DeviceType)
admin.site.register(DeviceCategory)
admin.site.register(DeviceVendor)
admin.site.register(DeviceOS)
admin.site.register(Device)
admin.site.register(DeviceManagement)
admin.site.register(DeviceInterface)
admin.site.register(DeviceTopology)
admin.site.register(DeviceConfiguration)
admin.site.register(DeviceFirmware01)

