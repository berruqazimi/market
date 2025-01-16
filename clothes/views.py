from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Garment
from .serializers import GarmentSerializer

class GarmentListView(generics.ListAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        garment_type = self.request.query_params.get('cloth_type')
        if garment_type:
            queryset = queryset.filter(cloth_type=garment_type)
        return queryset

class PublishGarmentView(generics.CreateAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class UnpublishGarmentView(generics.DestroyAPIView):
    queryset = Garment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        garment = self.get_object()
        if garment.publisher != request.user:
            return Response({"detail": "Not authorized to delete this garment."}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

class UpdateGarmentView(generics.UpdateAPIView):
    queryset = Garment.objects.all()
    serializer_class = GarmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        garment = self.get_object()
        if garment.publisher != self.request.user:
            raise PermissionError("Not authorized to update this garment.")
        serializer.save()
