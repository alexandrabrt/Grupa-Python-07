from django import forms

from customers.models import Companies
from locations.models import Location
from users.models import AuthUser


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'company_type', 'location']

    def __init__(self, auth_user_id, *args, **kwargs):
        super(CompaniesForm, self).__init__(*args, **kwargs)
        print(auth_user_id)
        # DenumireTabel.objects.filter() => returneaza 0 sau mai multe obiecte obiecte din db
        #                                  => in cazul in care nr de rezultate este 0, nu apare eroare
        #                                   => nu apare eroare nici in cazul in care sunt mai multe obiecte
        # DenumireTabel.objects.get() => returneaza 0 obiecte apare eroare
        #                             => returneaza mai mult de 1 rezultat apare iar eroare
        if AuthUser.objects.filter(is_active=True, id=auth_user_id, customer__isnull=False).exists():
            self.fields['location'] = forms.ModelChoiceField(queryset=Location.objects.filter(active=True,
                                                                                          id=AuthUser.objects.get(
                                                                                              id=auth_user_id).customer.location.id))


    def clean_name(self):
        name_value = self.cleaned_data.get('name')
        if Companies.objects.filter(name__exact=name_value).exists():
            raise forms.ValidationError('Compania deja exista. Te rugam sa alegi alt nume')
        return name_value

