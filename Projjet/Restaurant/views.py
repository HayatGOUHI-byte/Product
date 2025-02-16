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



# Passer une commande
def passer_commande_view(request, plat_id):
    plat = get_object_or_404(Plat, id=plat_id)
    if request.method == 'POST':
        client = get_object_or_404(Client, id=request.POST['client_id'])
        commande = Commande(client=client)
        commande.save()
        commande.plat.add(plat)
        commande.save()
        return HttpResponse("Commande passée avec succès!")
    return render(request, 'restaurant/passer_commande.html', {'plat': plat})




def client_commandes_view(request, client_id):
	client = get_object_or_404(Client, id=client_id)
	commandes = client.commandes.all()
	return render(request, 'restaurant/client_commandes.html', {'client': client, 'commandes': commandes})



#Récupérer tous les menus disponibles
def Menu_dispo(request):
	menus = Menu.objects.filter(disponible=True)
	return render(request,'restaurant/disponible.html',{'menus':menus})