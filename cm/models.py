from django.db import models

# Create your models here.

class TaskStatus(models.Model):
    status = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.status
    
class CheckpointPolicy(models.Model):
    policy = models.CharField(max_length=500, unique=True)
    site_name = models.ForeignKey('CheckpointSite', on_delete=models.CASCADE)

    def __str__(self):
        return self.policy

class CheckpointSite(models.Model):
    site_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.site_name

class CheckpointTask(models.Model):
    policy = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    source = models.CharField(max_length=1000)
    destination = models.CharField(max_length=1000)
    protocol = models.CharField(max_length=1000)
    schedule = models.CharField(max_length=1000)
    user_created = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE)
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.id
