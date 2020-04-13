from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=75,unique=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
