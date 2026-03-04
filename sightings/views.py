from rest_framework import generics, status
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Sighting, SightingConfirmation
from .serializers import SightingSerializer
from .permissions import CanCreateSighting, CanDeleteSighting, CanConfirmSighting

class SightingListCreateView(generics.ListCreateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
        created_by_id=self.request.user.id,
        created_by_role=self.request.user.role
    )

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), CanCreateSighting()]
        return [IsAuthenticated()]

class SightingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
    permission_classes = [IsAuthenticated, CanDeleteSighting]
    parser_classes = [MultiPartParser, FormParser]

class ConfirmSightingView(APIView):
    permission_classes = [IsAuthenticated, CanConfirmSighting]

    def post(self, request, pk):
        try:
            sighting = Sighting.objects.get(pk=pk)
        except Sighting.DoesNotExist:
            return Response({"detail": "Sighting not found"}, status=status.HTTP_404_NOT_FOUND)

        if sighting.created_by_id == request.user.id:
            return Response({"detail": "Cannot confirm your own sighting"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            SightingConfirmation.objects.create(
                sighting=sighting,
                user_id=request.user.id,
                user_role=request.user.role
            )
        except IntegrityError:
            return Response({"detail": "You have already confirmed this sighting"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Sighting confirmed"}, status=status.HTTP_200_OK)
