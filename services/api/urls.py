from django.urls import path

from .views import ServiceListView, ServiceDetailView

urlpatterns = [
    path('', ServiceListView.as_view()),
    path('<pk>', ServiceDetailView.as_view()),
]
