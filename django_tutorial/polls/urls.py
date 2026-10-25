from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zov', views.zov, name="zov"),
    path('<int:question_id>', views.detail, name="detail"),
]
