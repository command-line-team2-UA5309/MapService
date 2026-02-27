from django.http import JsonResponse
from django.urls import path, include

def home(request):
    return JsonResponse({"message": "Map Service is running"})

urlpatterns = [
    path('', home),
    path('api/sighting/', include('sightings.urls')),
]
