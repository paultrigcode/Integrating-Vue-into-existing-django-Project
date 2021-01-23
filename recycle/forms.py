from django.forms import ModelForm
from .models import Recycler

class RecyclerForm(ModelForm):
    class Meta:
        model = Recycler
        fields = ['id','first_name','last_name','street','phone_number','house_number']