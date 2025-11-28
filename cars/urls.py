from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('novo/', views.car_create, name='car_create'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
]
