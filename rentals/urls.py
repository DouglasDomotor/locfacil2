from django.urls import path
from .views import rental_list, rental_create, rental_finish

urlpatterns = [
    path('list/', rental_list, name='rental_list'),
    path('new/', rental_create, name='rental_create'),
    path('<int:rental_id>/finish/', rental_finish, name='rental_finish'),

]
