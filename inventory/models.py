from django.db import models

# Create your models here.

class DeviceLocation(models.Model):
    device_location = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_location
    
class DeviceType(models.Model):
    device_type = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_type
    
class DeviceCategory(models.Model):
    device_category = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_category
    
class DeviceVendor(models.Model):
    device_vendor = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_vendor
    
class DeviceBasicInfo(models.Model):
    device_name = models.CharField(max_length=200, blank=True)
    device_ip = models.GenericIPAddressField(unique=True)
    device_location = models.ForeignKey('DeviceLocation', on_delete=models.CASCADE)
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    device_category = models.ForeignKey('DeviceCategory', on_delete=models.CASCADE)
    device_vendor = models.ForeignKey('DeviceVendor', on_delete=models.CASCADE)
    device_description = models.CharField(max_length=200, blank=True)
    device_creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_ip

class DeviceManagement(models.Model):
    """Model definition for DeviceManagement."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    device_serial_number = models.CharField(max_length=100, blank=True)
    start_ma_date = models.DateField(blank=True)
    end_ma_date = models.DateField(blank=True)
    start_license_date = models.DateField(blank=True)
    end_license_date = models.DateField(blank=True)
    end_sw_support_date = models.DateField(blank=True)
    end_hw_support_date = models.DateField(blank=True)
    start_used_date = models.DateField(blank=True)

    def __str__(self):
        """Unicode representation of DeviceManagement."""
        return str(self.device_ip)

class DeviceInterface(models.Model):
    """Model definition for DeviceInterface."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    count_interface = models.IntegerField()
    list_interface_name = models.CharField(max_length=200, blank=True)
    list_interface_desc = models.CharField(max_length=200, blank=True)
    list_interface_inuse = models.CharField(max_length=200, blank=True)
    list_interface_unuse = models.CharField(max_length=200, blank=True)
    list_interface_speed = models.CharField(max_length=200, blank=True)
    list_interface_type = models.CharField(max_length=200, blank=True)
    list_interface_state = models.CharField(max_length=200, blank=True)
    list_interface_neighbor = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        """Unicode representation of DeviceInterface."""
        return str(self.device_ip)


class DeviceTopology(models.Model):
    """Model definition for DeviceTopology."""

    device_ip = models.ForeignKey('DeviceBasicInfo', on_delete=models.CASCADE)
    device_rack_name = models.CharField(max_length=200)
    device_rack_unit = models.IntegerField(max_length=200)
    
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