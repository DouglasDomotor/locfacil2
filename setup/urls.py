from django.contrib import admin
from django.urls import path, include
from cars.views import car_list
from cars.views import car_list, car_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('clients/', include('clients.urls')),
    path('cars/', car_list, name="car_list"),
    path('cars/<int:car_id>/', car_detail, name="car_detail"),
]
