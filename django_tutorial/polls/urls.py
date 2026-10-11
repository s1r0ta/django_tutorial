from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('vilka', views.vilka, name="vilka"),
    path('lozhka', views.lozhka, name="lozhka")
]
