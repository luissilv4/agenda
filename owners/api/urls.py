from django.urls import path

from .views import OwnerListCreateView, OwnerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', OwnerListCreateView.as_view()),
    path('<pk>', OwnerRetrieveUpdateDestroyAPIView.as_view()),
]
