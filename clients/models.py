from django.db import models
import uuid as uuid_lib

from staff.models import Staff

# Create your models here.

class Sex(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Sex"

    def __str__(self):
        return self.name




class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    alt_phone_number = models.IntegerField(blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING)
    data = models.DateField(auto_now=True)
    rgpd = models.BooleanField()
    birthday = models.DateField(blank=True, null=True)
    nif = models.IntegerField(blank=True, null=True)
    cc = models.CharField(max_length=15, blank=True)
    fav_staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, null=True, blank=True)
    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4,
           editable=False)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
