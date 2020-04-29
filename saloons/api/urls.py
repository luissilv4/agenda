from django.urls import path

from .views import SaloonListCreateView, SaloonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', SaloonListCreateView.as_view()),
    path('<pk>', SaloonRetrieveUpdateDestroyAPIView.as_view()),
]
