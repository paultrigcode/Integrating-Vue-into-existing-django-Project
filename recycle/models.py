from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
def increment_invoice_number():
	    last_customer_no = Recycler.objects.all().order_by('id').last()
	    if not last_customer_no:
	         return 1000
	    customer_no = last_customer_no.customer_number
	    customer_number_int = int(customer_no)
	    new_customer_number_int = customer_number_int + 1
	    return new_customer_number_int


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
    customer_number = models.IntegerField(max_length=1000000000,default=increment_invoice_number)

    def __str__(self):
        return self.first_name +" "+self.last_name



class Pickup(models.Model):
    date = models.DateField()
    recycler = models.ForeignKey(Recycler,on_delete=models.DO_NOTHING)
    collector = models.ForeignKey(to = get_user_model(),blank=True,null=True, on_delete=models.DO_NOTHING)
    points_updated = models.BooleanField(blank=True)
    points = models.IntegerField(blank=True, null=True, default=0)
    status = models.CharField(max_length = 100, default='Not Sent')

class Material(models.Model):
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    agent_percentage = models.FloatField(default=0.00)
    subscriber_percentage = models.FloatField(default=0.00)
    conversion = models.FloatField(default=1)
    collector_can_pickup = models.BooleanField(default = True)
    manager_can_pickup = models.BooleanField(default = True)
    def __str__(self):
        return self.name

class Item(models.Model):
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    pickup = models.ForeignKey(Pickup, on_delete=models.DO_NOTHING)
    weight = models.FloatField()
    points = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.material.name
