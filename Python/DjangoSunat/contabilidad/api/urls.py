from django.urls import path
from . import views

urlpatterns = [
    path('ruc', views.index, name='index'),
    path('nruc', views.Ruc,name="ruc")
]