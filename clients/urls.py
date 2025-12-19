from django.urls import path
from .views import client_list, client_detail, client_create

urlpatterns = [
    path('list/', client_list, name='client_list'),
    path('new/', client_create, name='client_create'),
    path('<int:client_id>/', client_detail, name='client_detail'),
]

