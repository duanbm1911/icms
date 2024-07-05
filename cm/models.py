from django.db import models

# Create your models here.

class CheckpointPolicy(models.Model):
    policy = models.CharField(max_length=200, unique=True)
    layer = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=100, blank=True, null=True)
    site = models.ForeignKey('CheckpointSite', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.policy

class CheckpointSite(models.Model):
    site = models.CharField(max_length=100, unique=True)
    smc = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.site

class CheckpointRule(models.Model):
    policy = models.ForeignKey('CheckpointPolicy', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    protocol = models.CharField(max_length=1000)
    schedule = models.CharField(max_length=1000, blank=True)
    user_created = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    
class F5Device(models.Model):
    f5_device_ip = models.CharField(max_length=200)
    f5_device_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.f5_device_ip)

class F5CreateVirtualServer(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    f5_template = models.ForeignKey('F5Template', on_delete=models.PROTECT)
    service_name = models.CharField(max_length=200)
    vs_name = models.CharField(max_length=200)
    vs_ip = models.GenericIPAddressField()
    vs_port = models.IntegerField()
    pool_name = models.CharField(max_length=200)
    pool_member = models.CharField(max_length=1000)
    pool_monitor = models.CharField(max_length=200)
    pool_lb_method = models.CharField(max_length=200)
    client_ssl_profile = models.CharField(max_length=200, blank=True)
    server_ssl_profile = models.CharField(max_length=200, blank=True)
    irules = models.CharField(max_length=200, blank=True)
    waf_profile = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    user_created = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.service_name)
    

class F5ClientSSLProfile(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    profile_name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.profile_name)
    
    
class F5ServerSSLProfile(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    profile_name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.profile_name)
    

class F5Irule(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    irule_name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.irule_name)

class F5WafProfile(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    waf_profile = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.waf_profile)
    
class F5PoolMemberMonitor(models.Model):
    f5_device_ip = models.ForeignKey('F5Device', on_delete=models.PROTECT)
    pool_monitor = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.pool_monitor)
    
class F5PoolMemberMethod(models.Model):
    pool_method = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.pool_method)

class F5Template(models.Model):
    template_name = models.CharField(max_length=200, unique=True)
    partition = models.CharField(max_length=200, blank=True)
    protocol = models.CharField(max_length=200, blank=True)
    client_protocol_profile = models.CharField(max_length=200, blank=True)
    server_protocol_profile = models.CharField(max_length=200, blank=True)
    client_http_profile = models.CharField(max_length=200, blank=True)
    server_http_profile = models.CharField(max_length=200, blank=True)
    snat_name = models.CharField(max_length=200, blank=True)
    http_analytics_profile = models.CharField(max_length=200, blank=True)
    tcp_analytics_profile = models.CharField(max_length=200, blank=True)
    http_compression_profile = models.CharField(max_length=200, blank=True)
    web_acceleration_profile = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return str(self.template_name)