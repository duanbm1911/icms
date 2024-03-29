from django.db import models

# Create your models here.

class CheckpointPolicy(models.Model):
    policy = models.CharField(max_length=500, unique=True)
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

class CheckpointTask(models.Model):
    policy = models.ForeignKey('CheckpointPolicy', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    protocol = models.CharField(max_length=1000)
    schedule = models.CharField(max_length=1000)
    user_created = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return str(self.id)
