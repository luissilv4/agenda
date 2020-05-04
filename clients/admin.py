from django.contrib import admin
from clients.models import Client, Sex, RGPD

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone_number')
admin.site.register(Client,ClientAdmin)
admin.site.register(Sex)
admin.site.register(RGPD)
