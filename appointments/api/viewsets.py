from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from datetime import datetime
from rest_framework import viewsets
from appointments.models import Appointment
from services.models import Service
from .serializers import (AppointmentListSerializer,
                         AppointmentSerializer, AppointmentListSerializer,
                         AppointmentStaffSerializer)



class AppointmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    list_serializer = AppointmentListSerializer
    permission_classes = (IsAuthenticated, )
    # filter_backends = (DjangoFilterBackend, OrderingFilter,)
    # detail_serializer_class = AppointmentDetailSerializer
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer
        return self.serializer_class

    # def create(self, request):
    #     pass

    def perform_create(self, serializer):
        service_id = (serializer.validated_data['service'])
        service_duration = Service.objects.get(pk=service_id.pk).duration
        serializer_duration = (serializer.validated_data['duration'])
        if serializer_duration == None:
            serializer.save(duration=service_duration)
        else:
            serializer.save(duration=serializer_duration)



    @action(detail=False)
    def get_staff_appointment(self, request, *args, **kwargs):
        appointments = Appointment.objects.filter(staff=self.kwargs['staff_pk'])
        appointments_json = AppointmentStaffSerializer(appointments, many=True)
        return Response(appointments_json.data)


    def update(self, request, uuid=None):
        instance = self.queryset.get(uuid=uuid)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        service_duration = Service.objects.get(pk=instance.service.pk).duration
        print(type(service_duration))
        duration = serializer.validated_data['duration']
        duration_str = duration.strftime("%H:%M:%S")
        print(duration_str)

        if duration_str == "00:00" or duration_str == "00:00:00":
            serializer.save(duration=service_duration)

        else:
            serializer.duration = duration
            serializer.save()

        return Response(serializer.data)

    #     """
    #     Determins which serializer to user `list` or `detail`
    #     """
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super().get_serializer_class()
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
