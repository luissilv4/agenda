from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientListCreateView.as_view()),
    # path('<pk>', ClientDetailView.as_view()),
    path('<uuid>', ClientRetrieveUpdateDestroyAPIView.as_view()),
]
