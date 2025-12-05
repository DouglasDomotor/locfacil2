from django.contrib import admin
from django.urls import path
from cars.views import car_list, car_detail, car_create, car_edit,car_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', car_list, name="car_list"),
    path('cars/new/', car_create, name="car_create"),
    path('cars/<int:car_id>/', car_detail, name="car_detail"),
    path('cars/<int:car_id>/edit/', car_edit, name="car_edit"),
    path('cars/<int:car_id>/delete/', car_delete, name='car_delete'),
]
