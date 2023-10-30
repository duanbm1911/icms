from django.contrib import admin
from inventory.models import *

# Register your models here.

admin.site.register(DeviceLocation)
admin.site.register(DeviceType)
admin.site.register(DeviceCategory)
admin.site.register(DeviceVendor)
admin.site.register(DeviceBasicInfo)
admin.site.register(DeviceManagement)
admin.site.register(DeviceInterface)
admin.site.register(DeviceTopology)
admin.site.register(DeviceConfiguration)

