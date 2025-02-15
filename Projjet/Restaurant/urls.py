from django.urls import path
from . import views



urlpatterns = [
path('', views.index, name='index'),
path('menu/', views.menu_view, name='menu_view'),
path('menu/<int:menu_id>/', views.menu_detail_view, name='menu_detail'),

]