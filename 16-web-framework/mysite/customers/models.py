from django.db import models

# Create your models here.

class Companies(models.Model):
    type_comp_choices = (('SRL', 'S.R.L.'),
                         ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=10, choices=type_comp_choices)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_type} {self.name}"
