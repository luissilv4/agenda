from django.urls import path

from .views import (AppointmentListCreateView, AppointmentDetailView,
                    AppointmentRetrieveUpdateDestroyAPIView)

app_name='appointments'
                    
urlpatterns = [
    path('', AppointmentListCreateView.as_view(), name='list'),
    # path('<pk>', AppointmentDetailView.as_view()),
    path('<uuid>', AppointmentRetrieveUpdateDestroyAPIView.as_view()),
]
