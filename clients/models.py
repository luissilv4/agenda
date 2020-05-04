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


class RGPD(models.Model):
    sms_reminders = models.BooleanField(default=False)
    email_reminders = models.BooleanField(default=False)
    new_appointment_notification = models.BooleanField(default=False)
    # anversarios e campanhas
    marketing = models.BooleanField(default=False)
    satisfaction_forms = models.BooleanField(default=False)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    alt_phone_number = models.IntegerField(blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING, related_name='client_sex')
    data = models.DateField(auto_now=True)
    rgpd = models.ForeignKey(RGPD, on_delete=models.DO_NOTHING, related_name='client_rgpd')
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

    def sex_name(self):
        return self.sex.name
