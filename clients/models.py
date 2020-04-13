from django.db import models
import uuid as uuid_lib


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
    sex = models.ForeignKey(Sex, on_delete=models.DO_NOTHING)
    data = models.DateField(auto_now=True)
    rgpd = models.BooleanField()
    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4,
           editable=False)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
