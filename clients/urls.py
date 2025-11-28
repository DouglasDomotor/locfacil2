from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('novo/', views.client_create, name='client_create'),
    path('<int:client_id>/', views.client_detail, name='client_detail'),
]
