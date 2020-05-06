from django.urls import path

from .views import (ServiceListCreateView, ServiceRetrieveUpdateDestroyAPIView,
                    )

urlpatterns = [
    path('', ServiceListCreateView.as_view()),
    path('<pk>', ServiceRetrieveUpdateDestroyAPIView.as_view()),
    # path('offices/', OfficeListCreateView.as_view())
]
