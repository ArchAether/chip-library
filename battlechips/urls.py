from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_number>/', views.mmbn6_by_id, name='by_id'),
    path('<str:name>/', views.mmbn_by_name, name='by_name'),
    path('elem/<str:elem>/', views.mmbn6_by_elem, name="by_elem"),
    path('desc/<str:description>/', views.mmbn6_by_description, name = "by_location"),
    path('', views.mmbn6_all, name='all'),
]