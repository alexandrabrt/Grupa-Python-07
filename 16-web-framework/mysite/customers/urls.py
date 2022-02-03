from django.urls import path

from customers import views

app_name = 'customers'

urlpatterns = [
    path('add/', views.CreateCompanyView.as_view(), name='adaugare')
]
