from django.urls import path
from . import views

urlpatterns= [
    path('', views.welcomeMessage, name="home"),
    path('message/<str:name>', views.showMessage, name= "message"),
]