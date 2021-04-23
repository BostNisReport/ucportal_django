from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
            
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
            
class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    s3bucket = models.TextField()
    s3region = models.TextField()
    s3key = models.TextField()

    class Meta:
        ordering = ('created',)
        
class UESession(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    log_name = models.CharField(max_length=100, blank=True, default='')
    version = models.CharField(max_length=100, blank=True, default='')
    machine_id = models.CharField(max_length=100 )
    activation_code = models.CharField(max_length=100,default='' )
    owner = models.ForeignKey(User, to_field='id')
    
    class Meta:
        ordering = ('created',)
        
class Object(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()
    
    class Meta:
        ordering = ('created',)

class Repository(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    remote_url = models.TextField()
    users = models.ManyToManyField(User) #Register which users have access to what servers (this is a cached value for faster lookups - it does not actually control security to the repository)
    
    class Meta:
        ordering = ('id',)
        
class UEFrameScenario(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    model = models.ForeignKey(Model, to_field='id')
    groups = models.ManyToManyField(Group) #Probably update this to groups
    users = models.ManyToManyField(User)
      
# class UEFrameSession(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    # session_id = models.CharField(max_length=100, blank=True, default='')
    # ue_frame_scenario = models.ForeignKey(UEFrameScenario, to_field='id')
    # expired = models.BooleanField( default=False )
    
    