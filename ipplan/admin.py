from django.contrib import admin
from ipplan.models import *

# Register your models here.

admin.site.register(Region)
admin.site.register(Location)
admin.site.register(Subnet)
admin.site.register(IpStatus)
admin.site.register(IpAddressModel)