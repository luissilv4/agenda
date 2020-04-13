from django.db import models
from clients.models import Client
from staff.models import Staff
from services.models import Service


# Create your models here.

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    notes = models.TextField(max_length=264, blank=True, null=True)
