from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated

from owners.models import Owner
from .serializers import OwnerSerializer


class OwnerListCreateView(ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = (IsAuthenticated, )


class OwnerDetailView(RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = (IsAuthenticated, )
