from rest_framework import serializers
from inventory.models import *

class DeviceConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfiguration
        fields = ['device_ip', 'device_config_standardized', 'device_monitored', 'device_backup_config', 'user_created']