from django.contrib import admin
from django.urls import path
from home import views

urlpatterns =[
   path('', views.index, name='home'),
   path("about/", views.about, name='about'),
   path("services/", views.services, name='services'),
  path("contact/", views.contact, name='contact'),
    #services Details
    path('party-order/', views.party_order, name='party_order'),
    path('family-pack/', views.family_pack, name='family_pack'),
    path('bulk-order/', views.bulk_order, name='bulk_order'),
]
