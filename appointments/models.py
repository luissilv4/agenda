from django.db import models
from clients.models import Client
from staff.models import Staff
from services.models import Service
import uuid as uuid_lib


# Create your models here.

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    duration = models.TimeField(null=True, blank=True)
    notes = models.TextField(max_length=264, blank=True, null=True)

    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4, editable=False)

    # def save(self, *args, **kwargs):
    #     if not self.duration:
    #         self.duration = self.service.duration
    #         super(Appointment, self).save(*args, **kwargs)
