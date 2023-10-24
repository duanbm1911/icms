from django.contrib import admin
from ipplan.models import *

# Register your models here.


admin.site.register(IpLocation)
admin.site.register(IpProject)
admin.site.register(IpSubnet)
admin.site.register(IpStatus)
admin.site.register(IpModel)