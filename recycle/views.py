from django.shortcuts import render
from .forms import RecyclerForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from .models import Recycler
from django.forms.models import model_to_dict
from datetime import date, timedelta
from django.db.models import Q
from .models import Pickup,Material,Item
import json




# Create your views here.


# class RecyclerView(View):
#     def post(self, request, *args, **kwargs):
#         json_request = QueryDict('', mutable=True)
#         json_request.update(json.loads(request.body))
#         form = RecyclerForm(json_request)
#         print(form)
#         if form.is_valid():
#             model = form.save()
#         return JsonResponse(data={"valid": False,"errors": form.errors},safe=False)
def update_pickup_points(pickup, household):
    """ Update households points with points from pickup 'pickup' """
    if not pickup and not household:
        return None

    if not pickup.points_updated:
        _current_points_ = household.current_points
        if _current_points_:
            new_points = _current_points_ + pickup.points
        else:
            new_points = pickup.points

        household.current_points = new_points
        try:
            household.save()
        except ElasticsearchException as e:
            pass # # Cant connect to elastic search
        except Exception as e:
            raise e

        pickup.points_updated = True
        pickup.save()
    return pickup


def convert_to_float(val):
  try:
    return float( val )
  except Exception as e:
    return float( re.sub("\D+",'', val ) )

def create_pickup_item(pickup_id, material_name, weight ):
  try:
    material = Material.objects.get(name=material_name)
    return ( Item.objects.create(pickup_id=pickup_id, weight=convert_to_float(weight), material_id=material.id ).weight, material.price )
  except Exception as e:
    return None

@login_required
def recycler_create(request):
    return render(request, 'create.html')

@login_required
def recycler_view(request):
    return render(request, 'view.html')




def create_recycler(request):
	data_list = []
	first_name = request.GET.get('first_name')
	if first_name == '2':
		print('hello')
	if first_name != '':
		data_list.append(first_name.strip())
	else:
		return HttpResponse('first_name cannot be blank',status=500)
	last_name = request.GET.get('last_name')
	if last_name != '':
		data_list.append(last_name.strip())
	else:
		return HttpResponse('last_name cannot be blank',status=500)
	street = request.GET.get('street')
	if street != '':
		data_list.append(street.strip())
	else:
		return HttpResponse('street cannot be blank',status=500)
	phone_number = request.GET.get('phone_number')
	if phone_number != '':
		data_list.append(phone_number.strip())
	else:
		return HttpResponse('phone_number cannot be blank',status=500)
	house_number =request.GET.get('house_number')
	if house_number !=  '':
		data_list.append(house_number)
	else:
		return HttpResponse('house_number cannot be blank',status=500)
	print(data_list)
	if len(data_list) !=5:
		return HttpResponse('Some fields data missing',status=500)
	elif Recycler.objects.filter(phone_number = phone_number.strip()).exists():
		return HttpResponse('phone_number already exists,please choose a unique phone_number',status=409)
	else:
		create_model = model_to_dict(Recycler.objects.create(first_name=first_name.strip(),last_name=last_name.strip(),street=street.strip(),house_number=house_number.strip(),phone_number=phone_number.strip(),date_joined=date.today()))
		print(create_model['customer_number'])		# customer_number = 
		return HttpResponse(create_model['customer_number'],content_type='text/plain',status=200)

def get_recycler(request):
    keyword = request.GET.get('keyword')
    if keyword != None:
        lookups= Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword) | Q(phone_number__icontains=keyword) |Q(customer_number__icontains=keyword)
        recycler =list(Recycler.objects.filter(lookups).values())
        if recycler == []:
        	return HttpResponse('No house Household details matches the search query,phone_number,customer-number,names, and current point',status=204)
    else:
        recycler = list(Recycler.objects.all().values())
    return JsonResponse(recycler,safe=False)

def pickup_create(request):
	return render(request,'pickup.html')

def auto_complete(request):
	return render(request,'auto.html')

def add_pickup(request,id):
    data = json.loads(request.body)
    print(data)
    print(data["PET"])
    print(data.items())

    print(id)
    pickup= Pickup()
    # pickup=Pickup.objects.create(recycler_id=id,collector = request.user, date = date.today(),points_updated = False)
    pickup.recycler_id = id
    pickup.collector = request.user
    pickup.date = date.today()
    pickup.points_updated = False
    pickup.save()

    total_points = 0


    for k, v in data.items():
        tmp = create_pickup_item(pickup.id, k, v)
        print(tmp)
        if tmp:
            total_points += int(round(round(tmp[0], 1) * tmp[1]))
    print(total_points)

    pickup.points = total_points
    pickup.save()
    update_pickup_points(pickup,pickup.recycler)
    response_data = {
       "data": "success",
    }	
   
    return HttpResponse('Succesfully sent Pickup',status=200)