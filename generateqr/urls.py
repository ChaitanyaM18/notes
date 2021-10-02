from django.urls import path
from . import views

app_name = 'generateqr'

urlpatterns = [
    path("home/",views.home,name="home"),
    path("genarate-qr/", views.generateQr, name="generateQr")
]
