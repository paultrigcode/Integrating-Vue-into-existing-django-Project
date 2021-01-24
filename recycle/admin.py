from django.contrib import admin

# Register your models here.
from .models import Recycler,Material,Pickup,Item
admin.site.register(Recycler)
admin.site.register(Material)
admin.site.register(Pickup)
admin.site.register(Item)

