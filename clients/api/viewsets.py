from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import (ClientSerializer, )
from clients.models import Client

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
    pagination_class = StandardResultsSetPagination
    # filter_backends = (DjangoFilterBackend, OrderingFilter,)
    # detail_serializer_class = AppointmentDetailSerializer
    lookup_field = 'uuid'

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return self.list_serializer
    #     return self.serializer_class


    # def get_queryset(self):
    #         """
    #         Optionally restricts the returned queries by filtering against
    #         a `sport` and `name` query parameter in the URL.
    #         """
    #         queryset = Match.objects.all()
    #         sport = self.request.query_params.get('sport', None)
    #         name = self.request.query_params.get('name', None)
    #         if sport is not None:
    #             sport = sport.title()
    #             queryset = queryset.filter(sport__name=sport)
    #         if name is not None:
    #             queryset = queryset.filter(name=name)
    #         return queryset
