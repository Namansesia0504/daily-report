from django.shortcuts import render
from rest_framework import generics
from .models import Medicine
from .newsecurity import IsSellerOrReadOnly
from .newnaman import MedicineSerializer

class MedicineListCreateView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all().order_by('-created_at')
    serializer_class = MedicineSerializer
    permission_classes = [IsSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class MedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsSellerOrReadOnly]

