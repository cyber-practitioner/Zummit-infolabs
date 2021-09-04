from django.urls import path,include
from django.shortcuts import redirect
from . import views
from django.contrib.auth import authenticate, login,logout

urlpatterns = [
    path('', views.home,name='home-page'),
    path('products', views.products,name='products-page'),
    path('orders',views.list_orders,name='list-orders'),
    path('consumer',views.consumers,name='list-customers'),
    path('login',views.signin,name='login-page'),
    path('forgot',views.forgot,name='forgot'),
    path('upload',views.upload,name='upload'),
    path('display',views.upload,name='upload-display'),

    path('specific-order',views.specific,name='spcific'),

    

]