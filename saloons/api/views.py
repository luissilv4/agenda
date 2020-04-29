from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated

from saloons.models import Saloon
from .serializers import SaloonSerializer


class SaloonListCreateView(ListCreateAPIView):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer
    permission_classes = (IsAuthenticated, )


class SaloonDetailView(RetrieveAPIView):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer


class SaloonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer
    permission_classes = (IsAuthenticated, )
