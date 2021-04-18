from django.urls import path, include
from django.contrib import admin
from shop import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('products', views.product),
    path('productview/<int:myid>/<int:price>' , views.productview),
    path('productview/<int:myid>/orderforme' , views.orderforme),
    path('gadgets', views.gadgets),
    path('cashback',views.cashbackform),
    path('gadgetsview',views.gadgetsview),
    
]
