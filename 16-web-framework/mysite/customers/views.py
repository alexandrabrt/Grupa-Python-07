from django.shortcuts import render

from django.urls import reverse
from django.views.generic import CreateView

from customers.forms import CompaniesForm
from customers.models import Companies


class CreateCompanyView(CreateView):
    model = Companies
    template_name = 'companies_form.html'
    form_class = CompaniesForm

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateCompanyView, self).form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateCompanyView, self).get_form_kwargs()
        kwargs.update({'auth_user_id': self.request.user.id})
        return kwargs

    def get_success_url(self):
        return reverse('customers:adaugare')
