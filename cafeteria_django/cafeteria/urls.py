from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('menu/',views.menu,name='menu'),
    path('cafes/', views.cafes,name='cafes'),
    path('baristas/',views.baristas,name='baristas'),
    path('reseñas/',views.reseñas,name='reseñas'),
    path('contacto/',views.contacto,name='contacto')
]
