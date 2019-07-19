from rest_framework import serializers
from bee.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'email')

class ApicultorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apicultor
        fields = ('url','nome', 'qtd_apiarios', 'tipo_criador', 'usuario')

class ApiarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apiario
        fields = ('url','apicultor', 'tipo', 'qtd_colmeias', 'localizacao')

class CaixaRacionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaixaRacional
        fields = ('url','apiario', 'identificador', 'especie')

class PerdaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perda
        fields = ('url','tipo_perda', 'qtd_colmeias_perdidas', 'data_registro_perda', 'especie_perdida', 'apiario')
        