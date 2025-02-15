from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Menu


def index(request):
	return HttpResponse("Welcome to Our Restaurant !")


def menu_view(request):
	menus = Menu.objects.all()
	return render(request,'restaurant/menu.html', {'menus':menus})