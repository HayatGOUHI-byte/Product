from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ProduitForm


from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseForbidden
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from.models import Produit
from .models import Categorie
from .models import Client
from .models import Commande
from .models import CustomerUser
from django import forms
#Afficher tous les produits
from monapp.forms import RechercheCategorieForm
from monapp.forms import OrdreForm

from monapp.forms import ContactForm
from django.shortcuts import redirect




class ProduitListView(ListView):
	model = Produit
	template_name = 'produit_list.html'
	context_object_name = 'produits'
class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm  # Utiliser le formulaire personnalisé
    template_name = 'produit_form.html'  # Le template pour le formulaire
    success_url = reverse_lazy('produit-list')  
class ProduitDeleteView(DeleteView):
	model = Produit 
	template_name = 'produit_confirm_delete.html'
	success_url = reverse_lazy('produit-list')

#détails d'un produit
class ProduitDetailView(DetailView):
	model = Produit
	template_name ='produit_detail.html'
	context_object_name = 'produit'
#Update un produit
class ProduitUpdateView(UpdateView):
	model = Produit
	form_class = ProduitForm
	template_name = 'produit_form.html'
	# fields = ['nom', 'prix']
	success_url = reverse_lazy('produit-list')
#Catégorie ********************
class CategorieCreateView(CreateView):
	model = Categorie
	template_name = 'categorie_form.html'
	fields = ['nom','description']
	success_url = reverse_lazy('categorie-list')
class CategorieListView(ListView):
	model = Categorie
	template_name = 'Categorie/categorie_list.html'
	context_object_name = 'categories'
class CategorieDetailView(DetailView):
	model = Categorie
	template_name = 'Categorie/categorie_detail.html'
	context_object_name = 'categorie' 
class CategorieDeleteView(DeleteView):
	model = Categorie
	template_name = 'Categorie/categorie_confirm_delete.html'
class CategorieUpdateView(UpdateView):
	model = Categorie
	template_name = 'Categorie/categorie_form.html'
	fields = ['nom','description']
	success_url = reverse_lazy('categorie-list')
class DisplaySpecificCategorie():
	model = Categorie
	template_name= 'Specific_Categorie.html'
	context_object_name = 'categorie'
def DisplaySpecificCategorie(request, pk):
	categorie  = get_object_or_404(Categorie, pk=pk)
	return render(request,'Categorie/Specific_Categorie.html', {'categorie':categorie})
def NumberInstanceCategorie(request):
	number = Categorie.objects.count()
	v = 15
	if number > 1000:
		return render(request,'Categorie/index.html',{'nombre':number,'valeur':v})
	else:
		return render(request,'Categorie/index.html')
def ReturnCategories(request):
	categories = Categorie.objects.all()  
	return render(request,'Categorie/AllCategories.html',{'categories' :categories})
def ReturnProducts(request):
	products = Produit.objects.all()
	return render(request, 'Product/AllProducts.html', {'products':products})

#***********FindByName************
def FindByName(request):
	produit = Produit.objects.get(nom="Lenovo")
	return render(request,'Product/FindByName.html',{'produit':produit})
def ProductsByCategorie(request):
	categorie = Categorie.objects.get(nom="Electronique")
	produits = Produit.objects.filter(categorie=categorie)
	return render(request,'Categorie/ProductsByCategorie.html', {'produits':produits,'categorie':categorie})
def OrderByPrice(request):
	produitsOrderByPrice  = Produit.objects.all().order_by('prix')
	return render(request,'Product/OrderByPrice.html', {'produitsOrderByPrice':produitsOrderByPrice})
def OrderByPriceA(request):
	produitsOrderByPriceA = Produit.objects.all().order_by('-prix')
	return render(request, 'Product/OrderByPriceA.html', {'produitsOrderByPriceA': produitsOrderByPriceA})
def CompterProduits(request):
	categorie = Categorie.objects.get(nom="Electronique")
	nombre_produits = Produit.objects.filter(categorie=categorie).count()
	return render(request,'Product/CompterProduits.html', {'nombre_produits':nombre_produits})

def ProductWithoutCategorie(request):
	produits = Produit.objects.filter(categorie=None)
	return render(request,'Product/ProductWithoutCategorie.html',{'produits':produits})






def rechercher_produits_par_categorie(request):
    produits = None  # Initialise à None pour éviter les erreurs avant la soumission du formulaire
    message = ""
    
    # Crée une instance du formulaire
    form = RechercheCategorieForm(request.POST or None)
    
    if request.method == 'POST':  # Si la requête est POST
        if form.is_valid():
            nom_categorie = form.cleaned_data['nom_categorie']
            
            # Rechercher les produits associés à la catégorie
            produits = Produit.objects.filter(categorie__nom__icontains=nom_categorie)
            if not produits.exists():
                message = f"Aucun produit trouvé pour la catégorie '{nom_categorie}'."
    
    # Retourne toujours une réponse HTTP
    return render(request, 'recherche_produits.html', {
        'form': form,
        'produits': produits,
        'message': message
    })


def liste_categories(request):
	categories= Categorie.objects.all()
	form = OrdreForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		colonne = form.cleaned_data['colonne']
		categories=categories.order_by(colonne)[:10]

	context = {
	'form' : form,
	'categories':categories
		}

	return render(request,'Categorie/liste_categories.html',context)	






def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Faites quelque chose avec les données ici (par exemple envoyer un email)
            client = Client(nom=nom, email=email, message = message)
            client.save()

            clients = Client.objects.all()
            number = clients.count()
            return render(request, 'contact.html', {'nom': nom,'email':email, 'message':message, 'clients':clients,'number':number})
    else:
        form = ContactForm()  # Créer un formulaire vide pour les requêtes GET

    # Retourner le formulaire (vide ou avec des données validées) pour les requêtes GET et POST
    return render(request, 'contact.html', {'form': form})


#ajouter une commande via la vue
def ajouter_commande(request):
	if request.method  == 'POST':
		client_id = request.POST.get('client_id')
		produit_id = request.POST.get('produit_id')
		quantite = int(request.POST.get('quantite'))


		client = get_object_or_404(Client, id=client_id)
		produit = get_object_or_404(Produit, id=produit_id)

		commande = Commande(client=client, produit=produit, quantite=quantite)
		commande.save()
		commandes = Commande.objects.all()
		return render(request,'Commande/index.html', {'commandes':commandes})

	clients = Client.objects.all()
	produits = Produit.objects.all()

	return render(request,'Categorie/commande_ajoutee.html', {'clients':clients, 'produits':produits})


def liste_Commande(request):
	commandes = Commande.objects.all()
	return render(request, 'Commande/index.html', {'commandes':commandes})


def delete_commande(request):
	Commande.objects.all().delete()
	return render(request,'Commande/index.html')


def supprimer_commande(request, client_id, produit_id):
	commande = get_object_or_404(Commande, client_id=client_id, produit_id=produit_id)
	commande.delete()
	return redirect('liste-Commande')


def register(request):
	if request.method == "POST":
		username= request.POST['username']
		email = request.POST['email']
		password = request.POST['password']


		hashed_password = make_password(password)
		user = CustomerUser.objects.create(username=username, email=email, password=hashed_password)
		return redirect('user_list')
	return render(request, 'Client/register.html')




#Afficher la lsite des utilisateurs

def user_list(request):
	if not request.user.is_authenticated:
		return HttpResponseForbidden("Vous devez êtes connecté")

	users = CustomerUser.objects.all()
	return render(request, 'Client/user_list.html', {'users': users})


def delete_user(request, user_id):
	if not request.user.is_authenticated or not request.user_is_admin:
		return HttpResponseForbidden("Interdit")

	user_to_delete = get_object_or_404(CustomerUser, id=user_id)
	user_to_delete.delete()
	return redirect('user_list')


def TousUtilisateur(request):
	users = CustomerUser.objects.all()
	return render(request,'Users/TousUtilisateur.html',{'users':users})
