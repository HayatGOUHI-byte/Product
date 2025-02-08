from django.shortcuts import render, get_object_or_404
from .forms import ProduitForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from.models import Produit
from .models import Categorie
from django import forms
#Afficher tous les produits

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
	TousLesCategories = Categorie.objects.all()
	return render(request,'Product/CompterProduits.html', {'TousLesCategories':TousLesCategories})