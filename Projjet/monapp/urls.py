from django.urls import path


from .views import(
	ProduitListView,  choisir_produit,
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
	FindByName,ajouter_commande,
	ProductsByCategorie,contact,
	OrderByPrice, OrderByPriceA,CompterProduits,
	ProductWithoutCategorie, rechercher_produits_par_categorie,liste_categories,search_user,
	liste_Commande,delete_commande,supprimer_commande,register,user_list,delete_user,TousUtilisateur,userdetail,
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
path('categories/', liste_categories, name='liste_categories' ),
path('contact/',contact, name='contact'),
path('ajouter_commande',ajouter_commande, name='ajouter_commande'),
#client*****************

path('register/',register, name="register"),
path('users/', user_list, name='user_list'),
path('delete_user/<int:user_id>/',delete_user, name='delete_user'),

#commande****************
path('liste_Commande', liste_Commande, name='liste-Commande'),
path('delete_commande', delete_commande, name='delete_commande'),
path('commandes/supprimer/<int:client_id>/<int:produit_id>/', supprimer_commande, name='supprimer_commande'),
#Users***************************************
path('Users/TousUtilisateur/', TousUtilisateur, name='TousUtilisateur'),
path('Client/userdetail/<str:username>/', userdetail, name='userdetail'),
path('search-user/', search_user, name='search_user'),
 path('choisir_produit/<int:client_id>/', choisir_produit, name='choisir_produit'),
]



