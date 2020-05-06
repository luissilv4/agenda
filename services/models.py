from django.db import models

# Create your models here.


class Office(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=75,unique=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    office = models.ManyToManyField(Office)

    def __str__(self):
        return self.name
