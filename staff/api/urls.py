from django.urls import path

from .views import StaffListView, StaffDetailView

urlpatterns = [
    path('', StaffListView.as_view()),
    path('<pk>', StaffDetailView.as_view()),
]
