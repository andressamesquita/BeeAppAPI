from django.shortcuts import render
from rest_framework import viewsets
from bee.serializers import *
from bee.models import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ApicultorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Apicultor.objects.all()
    serializer_class = ApicultorSerializer

class ApiarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apiario.objects.all()
    serializer_class = ApiarioSerializer

class CaixaRacionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CaixaRacional.objects.all()
    serializer_class = CaixaRacionalSerializer

class PerdaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Perda.objects.all()
    serializer_class = PerdaSerializer
