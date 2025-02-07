from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated

from services.models import Service, Office
from .serializers import ServiceSerializer, OfficeSerializer


class ServiceListCreateView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated, )


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated, )




class OfficeListCreateView(ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated, )


class OfficeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated, )
