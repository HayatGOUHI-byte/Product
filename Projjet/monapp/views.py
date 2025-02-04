from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from.models import Produit


#Afficher tous les produits

class ProduitListView(ListView):
	model = Produit
	template_name = 'produit_list.html'
	context_object_name = 'produits'


#ajouter un produit
class ProduitCreateView(createView):
	model = Produit 
	template_name = 'produit_form.html'
	fileds = ['nom','prix']
	sucess_url = reverse_lazy('produit-list')


#supprimer un produit
class ProduitDeleteView(DelteView):
	model = Produit 
	template_name = 'produit_confirm_delete.html'
	success_url = reverse_lazy('produit-list')

#détails d'un produit

class ProduitDetailView(DetailView):
	model = Produit
	template_name ='produit_detail.html'
	context_object_name = 'produit'