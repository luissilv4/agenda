from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                    ListAPIView, CreateAPIView)

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from appointments.models import Appointment
from .serializers import (AppointmentListSerializer,
                         AppointmentSerializer, AppointmentListSerializer)


# class AppointmentListView(ListAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentListSerializer
#     permission_classes = (IsAuthenticated, )
#     lookup_field = 'uuid'
#
#
# class AppointmentCreateView(CreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentCreateSerializer
#     permission_classes = (IsAuthenticated, )
#     lookup_field = 'uuid'
#
#
# class AppointmentDetailView(RetrieveAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentListSerializer
#
#
# class AppointmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentCreateSerializer
#     permission_classes = (IsAuthenticated, )
#     lookup_field = 'uuid'


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, )
    # filter_backends = (DjangoFilterBackend, OrderingFilter,)
    # detail_serializer_class = AppointmentDetailSerializer
    lookup_field = 'uuid'

    # def get_serializer_class(self):
    #     """
    #     Determins which serializer to user `list` or `detail`
    #     """
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super().get_serializer_class()



#
# class AppoinmentViewSeta(viewsets.ModelViewSet):
#     """
#     retrieve:
#     Return the given match.
#     list:
#     Return a list of all the existing appointments.
#     create:
#     Create a new appointment instance.
#     """
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentListSerializer # for list view
#     detail_serializer_class = AppointmentDetailSerializer # for detail view
#     filter_backends = (DjangoFilterBackend, OrderingFilter,)
#     ordering_fields = '__all__'
#     def get_serializer_class(self):
#         """
#         Determins which serializer to user `list` or `detail`
#         """
#         if self.action == 'retrieve':
#             if hasattr(self, 'detail_serializer_class'):
#                 return self.detail_serializer_class
#         return super().get_serializer_class()
#     def get_queryset(self):
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
#     def create(self, request):
#         """
#         to parse the incoming request and create a new match or update
#         existing odds.
#         """
#         message = request.data.pop('message_type')
#         # check if incoming api request is for new event creation
#         if message == "NewEvent":
#             event = request.data.pop('event')
#             sport = event.pop('sport')
#             markets = event.pop('markets')[0] # for now we have only one market
#             selections = markets.pop('selections')
#             sport = Sport.objects.create(**sport)
#             markets = Market.objects.create(**markets, sport=sport)
#             for selection in selections:
#                 markets.selections.create(**selection)
#             match = Match.objects.create(**event, sport=sport, market=markets)
#             return Response(status=status.HTTP_201_CREATED)
#         # check if incoming api request is for updation of odds
#         elif message == "UpdateOdds":
#             event = request.data.pop('event')
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             for selection in selections:
#                 s = Selection.objects.get(id=selection['id'])
#                 s.odds = selection['odds']
#                 s.save()
#             match = Match.objects.get(id=event['id'])
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
