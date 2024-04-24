from rest_framework import viewsets, filters
from vinny.models import Frase
from vinny.serializers import FraseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class FraseViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['text']
    search_fields = ['text']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]