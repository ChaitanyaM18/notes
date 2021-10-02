from django.urls import path
from . import views

urlpatterns = [
    path('addcategory/', views.categoryForm, name='categoryForm'),
    path('addmenuitems', views.MenuForm, name='MenuForm')
]
