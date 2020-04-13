from django.contrib import admin
from clients.models import Client, Sex

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone_number','rgpd')
admin.site.register(Client,ClientAdmin)
admin.site.register(Sex)
