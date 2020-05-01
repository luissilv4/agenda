from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .viewsets import AppointmentViewSet
# from .views import (AppointmentCreateView, AppointmentListView,
#                     AppointmentRetrieveUpdateDestroyAPIView)

app_name='appointments'
#
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

appointments_list = AppointmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
appointment_detail = AppointmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
appointment_staff_list = AppointmentViewSet.as_view({
    'get': 'get_staff_appointment'
})


urlpatterns = format_suffix_patterns([
    path('', appointments_list, name='appointments-list'),
    path('<uuid>/', appointment_detail, name='appointment-detail'),

    path('staff/<int:staff_pk>/', appointment_staff_list, name='appointment-staff'),
])



# urlpatterns = [
#     # path('', include(router.urls)),
#     path('', AppointmentListView.as_view(), name='list'),
#     path('add', AppointmentCreateView.as_view(), name='add'),
#     # path('<pk>', AppointmentDetailView.as_view()),
#     path('<uuid>', AppointmentRetrieveUpdateDestroyAPIView.as_view()),
# ]
