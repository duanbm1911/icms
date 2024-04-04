from django.contrib import admin
from cm.models import *

# Register your models here.

admin.site.register(CheckpointRule)
admin.site.register(CheckpointSite)
admin.site.register(CheckpointPolicy)