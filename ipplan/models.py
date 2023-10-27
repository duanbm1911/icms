from django.db import models

# Create your models here.

class IpRegoin(models.Model):
    """Model definition for IpRegoin."""

    regoin = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpRegoin."""
        return self.regoin



class IpLocation(models.Model):
    """Model definition for IpLocation."""

    location = models.CharField(max_length=100)
    regoin = models.ForeignKey('IpRegoin', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpLocation."""
        return self.location


class IpSubnet(models.Model):
    """Model definition for IpSubnet."""

    subnet = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey('IpLocation', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpSubnet."""
        return self.subnet


class IpAddressModel(models.Model):
    """Model definition for IpModel."""

    ip_address = models.GenericIPAddressField()
    subnet = models.ForeignKey('IpSubnet', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    user_request = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)


    def __str__(self):
        """Unicode representation of IpModel."""
        return self.ip_address



