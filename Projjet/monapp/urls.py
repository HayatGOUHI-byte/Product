from django.urls import path


from .views import(
	ProduitListView,
	ProduitCreateView,
	ProduitUpdateView,
	ProduitDeleteView,
	ProduitDetailView,
	)


urlpatterns =  [
path('',ProduitListView.as_view(), name='produit-list'),
path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
path('produit/ajouter/', ProduitCreateView.as_view(), name='produit-create'),
path('produit/<int:pk>/modifier/', ProduitUpdateView.as_view(), name='produit-update'),
path('produit/<int:pk>/supprimer/',ProduitDeleteView.as_view(), name='produit-delete'),
]