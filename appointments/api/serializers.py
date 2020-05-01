from rest_framework import serializers
from appointments.models import Appointment
from clients.models import Client
from staff.models import Staff
from services.models import Service

from clients.api.serializers import ClientSerializer
from services.api.serializers import ServiceSerializer
from staff.api.serializers import StaffSerializer



class AppointmentStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['client','service','date','duration','notes','uuid']



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['client','staff','service','date','duration','notes','uuid']



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')



class AppointmentListSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    service = ServiceSerializer()
    staff = StaffSerializer()

    class Meta:
        model = Appointment
        fields = ['service','date','staff','client','duration','uuid','notes']
