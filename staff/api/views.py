from rest_framework.generics import ListAPIView, RetrieveAPIView

from staff.models import Staff
from .serializers import StaffSerializer


class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
