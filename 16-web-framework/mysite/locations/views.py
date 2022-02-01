# Create your views here.
# CreateView => adauga inregistrari in baza de date
# UpdateView => modifica inregistrari in baza de date
# IndexView => listeaza inregistrarile din baza de date
# ListView => listeaza toate inregistrarile din baza de date
# DeleteView => sterge inregistrarile din baza de date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from locations.models import Location

class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = '__all__' # le afisam pe toate din models
    fields = ['city', 'country'] # daca dorim sa numim doar anumite campuri pentru vizualizare
    template_name = 'locations_form.html'

    def get_success_url(self):
        return reverse('locations:adauga')


class LocationsView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'locations_index.html'

    def get_queryset(self):
        return Location.objects.filter(active=True)


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'locations_form.html'

    def get_queryset(self):
        return Location.objects.filter(active=True)

    def get_success_url(self):
        return reverse('locations:lista_locatii')

@login_required
def deactivate_locations(request, pk):
    if Location.objects.filter(id=pk).exists():
        Location.objects.filter(id=pk).update(active=False)
    return redirect('locations:lista_locatii')
