from django.db import models
from owners.models import Owner
# Create your models here.


class Saloon(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    nif = models.IntegerField()
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
