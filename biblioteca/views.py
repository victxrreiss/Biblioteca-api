# TODO: implementação pendente — responsabilidade de outro integrante do grupo.

from rest_framework import viewsets
from .models import Autor,Livro
from .serializers import AutorSerializer, LivroSerializer, AutorResumoSerializer, LivroResumoSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorResumoViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorResumoSerializer

class LivroResumoViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroResumoSerializer