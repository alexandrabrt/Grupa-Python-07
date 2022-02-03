from django.shortcuts import render

from django.urls import reverse
from django.views.generic import CreateView

from customers.models import Companies


class CreateCompanyView(CreateView):
    model = Companies
    template_name = 'companies_form.html'
    fields = '__all__'

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateCompanyView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('customers:adaugare')
