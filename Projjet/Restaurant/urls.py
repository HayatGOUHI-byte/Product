from django.urls import path
from . import views






urlpatterns = [
path('', views.index, name='index'),
path('menu/', views.menu_view, name='menu_view'),
path('menu/<int:menu_id>/', views.menu_detail_view, name='menu_detail'),
path('commande/<int:plat_id>/', views.passer_commande_view, name='passer_commande'),
path('client/<int:client_id>/commandes/', views.client_commandes_view, name='client_commandes'),
path('disponible/', views.Menu_dispo, name='Menu_dispo'),
path('quelle_menu/',views.afficher_plat, name='afficher_plat'),
path('index/', views.Client_Plat, name='Client_Plat'),
path('details/<int:id>/', views.detail, name='detail'),
 path('recherche-commandes/', views.rechercher_commandes, name='rechercher_commandes'),

]