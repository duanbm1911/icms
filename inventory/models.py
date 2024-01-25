from django.db import models

# Create your models here.

class DeviceLocation(models.Model):
    device_location = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_location
    
class DeviceType(models.Model):
    device_type = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_type
    
class DeviceCategory(models.Model):
    device_category = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_category
    
class DeviceVendor(models.Model):
    device_vendor = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_vendor
    
class DeviceBasicInfo(models.Model):
    device_name = models.CharField(max_length=250, blank=True)
    device_ip = models.GenericIPAddressField(unique=True)
    device_location = models.ForeignKey('DeviceLocation', on_delete=models.CASCADE)
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    device_category = models.ForeignKey('DeviceCategory', on_delete=models.CASCADE)
    device_vendor = models.ForeignKey('DeviceVendor', on_delete=models.CASCADE)
    device_description = models.CharField(max_length=250, blank=True)
    device_creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_ip

class DeviceManagement(models.Model):
    """Model definition for DeviceManagement."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    device_serial_number = models.CharField(max_length=100)
    start_ma_date = models.DateField()
    end_ma_date = models.DateField()
    start_license_date = models.DateField()
    end_license_date = models.DateField()
    end_sw_support_date = models.DateField()
    end_hw_support_date = models.DateField()
    start_used_date = models.DateField()

    def __str__(self):
        """Unicode representation of DeviceManagement."""
        return str(self.device_ip)

class DeviceInterface(models.Model):
    """Model definition for DeviceInterface."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    count_interface = models.IntegerField()
    list_interface_name = models.JSONField()
    list_interface_desc = models.JSONField()
    list_interface_inuse = models.JSONField()
    list_interface_unuse = models.JSONField()
    list_interface_speed = models.JSONField()
    list_interface_type = models.JSONField()
    list_interface_state = models.JSONField()
    list_interface_neighbor = models.JSONField()
    
    def __str__(self):
        """Unicode representation of DeviceInterface."""
        return str(self.device_ip)


class DeviceTopology(models.Model):
    """Model definition for DeviceTopology."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    device_rack_name = models.CharField(max_length=250)
    device_rack_unit = models.CharField(max_length=250)
    
    def __str__(self):
        """Unicode representation of DeviceTopology."""
        return str(self.device_ip)
    

class DeviceConfiguration(models.Model):
    """Model definition for DeviceConfiguration."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    device_config_standardized = models.BooleanField()
    device_monitored = models.BooleanField()
    device_backup_config = models.BooleanField()

    def __str__(self):
        """Unicode representation of DeviceConfiguration."""
        return str(self.device_ip)