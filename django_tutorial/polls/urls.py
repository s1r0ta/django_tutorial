from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('vilka', views.vilka, name="vilka"),
    path('lozhka', views.lozhka, name="lozhka")
=======
    path('<int:question_id>', views.detail, name="detail"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='results'),
>>>>>>> 55b8074
]
