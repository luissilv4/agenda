from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated

from appointments.models import Appointment
from .serializers import AppointmentSerializer


class AppointmentListCreateView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'


class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'
