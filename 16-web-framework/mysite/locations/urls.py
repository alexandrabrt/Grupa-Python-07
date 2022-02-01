from django.urls import path
from locations import views

app_name = 'locations'

urlpatterns = [
    path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
    path('', views.LocationsView.as_view(), name='lista_locatii'),
    path('modificare/<int:pk>/', views.UpdateLocationView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_locations, name='dezactiveaza'),
]
