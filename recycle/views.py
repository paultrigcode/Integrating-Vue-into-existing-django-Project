from django.shortcuts import render
from .forms import RecyclerForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from .models import Recycler
from django.forms.models import model_to_dict
from datetime import date, timedelta
from django.db.models import Q




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
		Recycler.objects.create(first_name=first_name.strip(),last_name=last_name.strip(),street=street.strip(),house_number=house_number.strip(),phone_number=phone_number.strip(),date_joined=date.today())
		return HttpResponse('Success',status=200)

def get_recycler(request):
    keyword = request.GET.get('keyword')
    if keyword != None:
        lookups= Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword) | Q(phone_number__icontains=keyword)
        recycler =list(Recycler.objects.filter(lookups).values())
        if recycler == []:
        	return HttpResponse('No house Household details matches the search query,phone_number,customer-number,names, and current point',status=204)
    else:
        recycler = list(Recycler.objects.all().values())
    return JsonResponse(recycler,safe=False)


