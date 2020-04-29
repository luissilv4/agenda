from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                    ListAPIView, CreateAPIView)

from rest_framework.permissions import IsAuthenticated

from appointments.models import Appointment
from .serializers import (AppointmentListSerializer,
                         AppointmentCreateSerializer, AppointmentListSerializer)


class AppointmentListView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'


class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'


class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer


class AppointmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'
