from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Staff'
        
    def __str__(self):
        return self.name
