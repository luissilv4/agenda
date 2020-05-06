from django.urls import path

from .views import (ServiceListCreateView, ServiceRetrieveUpdateDestroyAPIView,
                    OfficeListCreateView, OfficeRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', ServiceListCreateView.as_view()),
    path('offices/', OfficeListCreateView.as_view()),
    path('offices/<pk>', ServiceRetrieveUpdateDestroyAPIView.as_view()),
    path('<pk>', ServiceRetrieveUpdateDestroyAPIView.as_view()),
]
