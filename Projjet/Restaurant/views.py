from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Menu


def index(request):
	return HttpResponse("Welcome to Our Restaurant !")


def menu_view(request):
	menus = Menu.objects.all()
	return render(request,'restaurant/menu.html', {'menus':menus})

#menu_detail
def menu_detail_view(request, menu_id):
	menu = get_object_or_404(Menu, id=menu_id)
	plats = menu.plats.all()
	return render(request,'restaurant/menu_detail.html',{'menu':menu, 'plats':plats})