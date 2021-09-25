from django.urls import path

from . import views

urlpatterns = [
    path('mmbn6/', views.mmbn6_all, name='mmbn6_all'),
    # path('', views.index, name='index'),
]