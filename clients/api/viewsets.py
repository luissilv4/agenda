from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import (ClientSerializer, )
from clients.models import Client
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter




class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000





class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    # pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('name', 'phone_number', 'id', 'cc', 'nif')
    ordering_fields = ('id','name')
    ordering = ('name')
    # detail_serializer_class = AppointmentDetailSerializer
    lookup_field = 'uuid'
