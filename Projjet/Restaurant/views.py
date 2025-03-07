from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Menu, Plat
from .models import Client
import json
from .models import Commande
from django.shortcuts import render, get_object_or_404

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



def afficher_plat(request):
	plats = Plat.objects.all()
	menu_plat = None

	if request.method=='POST':
		plat_id = int(request.POST.get('plat'))
		plat_selectionne = Plat.objects.get(id=plat_id)
		menu_plat = plat_selectionne.menu
	return render(request, 'restaurant/quelle_menu.html', {'plats': plats, 'menu_plat': menu_plat})




def Client_Plat(request):
	clients = Client.objects.all()
	plats = Plat.objects.all()
	return render(request,'restaurant/index.html', {'clients':clients,'plats':plats})

def detail(request,id):
	plat = get_object_or_404(Plat, id=id)
	return render(request, 'restaurant/index.html', {'plat':plat})


def addition(a,b):
	return a+b

def JSON_Convert(request):
	json_data = '{"nom":"Alice", "age":25}'
	data = json.loads(json_data)

	python_dict = {"nom": "Bob", "age": 30}
	json_string = json.dumps(python_dict, indent=4)
	


def convert_JSON(request):
	jason_data = '{"nom":"Alice", "age":25}'
	data = json.loads(jason_data)


def Test_de_fonction(request):
	chaine_de_caractere = 'this is my file'
	print(chaine_de_caractere[1])

#on va récupérer les commandes associés à un plat X

def rechercher_commandes(request):
	commandes=None
	query = request.GET.get('nom_plat')
	if query:
		try:
			plat = Plat.objects.get(nom__iexact=query)
			commandes = plat.commandes.all()
		except Plat.DoesNotExist:
			commandes = []

	return render(request,'restaurant/rechercher_commandes.html', {'commandes':commandes, 'query':query})



def rechercher_commande(request):
	commande = None
	query = request.GET.get('id_commande')

	if query:
		try:
			commande = Commande.objects.get(id=query)
		except Commande.DoesNotExist:
			commande = None

	return render(request, 'restaurant/rechercher_commande.html',{'commande':commande, 'query':query})