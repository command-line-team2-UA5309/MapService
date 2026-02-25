from django.urls import path
from .views import SightingListCreateView, SightingDetailView, ConfirmSightingView

urlpatterns = [
    path('', SightingListCreateView.as_view(), name='sighting-list-create'),
    path('<int:pk>/', SightingDetailView.as_view(), name='sighting-detail'),
    path('<int:pk>/confirm/', ConfirmSightingView.as_view(), name='sighting-confirm'),
]