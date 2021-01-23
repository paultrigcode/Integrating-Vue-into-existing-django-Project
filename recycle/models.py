from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Recycler(models.Model): 
    class Meta:
        ordering = ['id']
    user = models.OneToOneField(to=get_user_model(),related_name='recycler', on_delete=models.DO_NOTHING, blank=True,null=True)
    collector = models.ForeignKey(to=get_user_model(),related_name="collector", blank=True, null=True, on_delete=models.DO_NOTHING)
    current_points = models.IntegerField(null=True,blank=True,default=0)
    redeemable = models.IntegerField(null=True,blank=True)
    house_number = models.CharField(max_length=20, null=True,blank=True)
    street = models.CharField(max_length = 200, null=True, blank=True)
    first_name = models.CharField(max_length=50, default = ' ')
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length=12, null=True, blank=True) 
    active = models.BooleanField(default=True)
    date_joined = models.DateField()
    num_pickups = models.IntegerField(default=0)
    total_pickups = models.IntegerField(default=0)
    customer_number = models.IntegerField(default=0)
    