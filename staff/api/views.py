from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                    RetrieveAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated
from staff.models import Staff
from .serializers import StaffSerializer


class StaffListView(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated, )


class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated, )
