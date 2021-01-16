from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, JsonResponse, QueryDict

# Create your views here.

def search(request):
	title = request.GET.get('title')
	print(title)
	post = list(Post.objects.filter(title__icontains=title).values())
	return JsonResponse(post,safe=False)


