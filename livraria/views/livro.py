from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from livraria.models import Livro
from livraria.serializers import LivroSerializer, LivroDetailSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao","editora__Nome"]
    search_fields = ["titulo"]
    ordering_fields = ["titulo", "preco"]
    ordering = ["titulo"]
    
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
    
    