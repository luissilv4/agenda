from django.urls import path

from .views import (AppointmentCreateView, AppointmentListView,
                    AppointmentRetrieveUpdateDestroyAPIView)

app_name='appointments'

urlpatterns = [
    path('', AppointmentListView.as_view(), name='list'),
    path('add', AppointmentCreateView.as_view(), name='add'),
    # path('<pk>', AppointmentDetailView.as_view()),
    path('<uuid>', AppointmentRetrieveUpdateDestroyAPIView.as_view()),
]
