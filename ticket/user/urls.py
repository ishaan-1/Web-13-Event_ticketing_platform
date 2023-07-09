from django.contrib import admin
from django.urls import path 
from django import views
from user import views


urlpatterns = [
    path('',views.index,name="home"),
    path('profile/',views.personalprofile,name='personalprofile'),
      path('profile/edit/',views.editprofile,name='editprofile'),
      path('profile/pep/',views.pep,name='pep'),
      path('profile/pep/cart',views.cart,name='cart')
]
