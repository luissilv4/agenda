from django.urls import path

from .views import (AppointmentListCreateView, AppointmentDetailView,
                    AppointmentRetrieveUpdateDestroyAPIView)
urlpatterns = [
    path('', AppointmentListCreateView.as_view()),
    # path('<pk>', AppointmentDetailView.as_view()),
    path('<uuid>', AppointmentRetrieveUpdateDestroyAPIView.as_view()),
]
