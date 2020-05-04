from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ClientListCreateView, ClientRetrieveUpdateDestroyAPIView
from .viewsets import ClientViewSet

app_name='clients'

clients_list = ClientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

client_detail = ClientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', clients_list, name='clients-list'),
    path('<uuid>', client_detail, name='client-detail'),
])
