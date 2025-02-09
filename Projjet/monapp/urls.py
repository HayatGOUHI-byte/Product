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
	DisplaySpecificCategorie,
	NumberInstanceCategorie,
	ReturnCategories,
	ReturnProducts,
	FindByName,
	ProductsByCategorie,
	OrderByPrice, OrderByPriceA,CompterProduits,
	ProductWithoutCategorie, rechercher_produits_par_categorie,
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
path('Categorie/<int:pk>/', DisplaySpecificCategorie, name='specific-categorie'),
path('Categorie/count/',NumberInstanceCategorie, name='nombreInstanceCategorie'),
path('Categorie/CountCategories/',ReturnCategories,  name='returnCategories'),
path('Product/AllProducts/', ReturnProducts, name='returnProducts'),
path('Product/FindByName/', FindByName, name='FindByName'),
path('Categorie/ProductsByCategorie', ProductsByCategorie, name='ProductsByCategorie'),
path('Product/OrderByPrice', OrderByPrice, name='OrderByPrice'),
path('Product/OrderByPriceA', OrderByPriceA, name='OrderByPriceA'),
path('Product/CompterProduits', CompterProduits, name='CompterProduits'),
path('Product/ProductWithoutCategorie', ProductWithoutCategorie, name='ProductWithoutCategorie'),
path('rechercher/', rechercher_produits_par_categorie, name='rechercher-produits-par-categorie'),
]



