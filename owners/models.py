from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    nif = models.IntegerField()
    phone = models.IntegerField()
    alt_phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname
