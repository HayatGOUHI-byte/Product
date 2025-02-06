from django.urls import path


from .views import(
	ProduitListView,
	ProduitCreateView,
	ProduitUpdateView,
	ProduitDeleteView,
	ProduitDetailView,
	CategorieListView,
	CategorieDetailView,
	CategorieDeleteView,
	CategorieUpdateView,
	CategorieCreateView,
	)



urlpatterns =  [
path('',ProduitListView.as_view(), name='produit-list'),
path('produit/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
path('produit/ajouter/', ProduitCreateView.as_view(), name='produit-create'),
path('produit/<int:pk>/modifier/', ProduitUpdateView.as_view(), name='produit-update'),
path('produit/<int:pk>/supprimer/',ProduitDeleteView.as_view(), name='produit-delete'),
path('Categorie/',CategorieListView.as_view(), name='categorie-list'),

path('Categorie/categorie/<int:pk>/', CategorieDetailView.as_view(), name='categorie-detail'),
path('Categorie/categorie/ajouter/', CategorieCreateView.as_view(), name='categorie-create'),
path('Categorie/categorie/<int:pk>/modifier/', CategorieUpdateView.as_view(), name='categorie-update'),
path('Categorie/categorie/<int:pk>/supprimer/',CategorieDeleteView.as_view(), name='categorie-delete'),

]