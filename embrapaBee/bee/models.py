from django.db import models
from django.contrib.auth.models import User

class Apicultor(models.Model):
    TIPO_CRIADOR_CHOICES = (
        ('PESQUISADOR', 'Pesquisador'),
        ('CRIADOR AUTÔNOMO', 'Criador autônomo'),
        ('PRODUTOR DE MEL', 'Produtor de mel'),
    )

    nome = models.CharField(max_length=255, null=False)
    qtd_apiarios = models.IntegerField()
    tipo_criador = models.CharField(max_length=16, choices=TIPO_CRIADOR_CHOICES, null=False, blank=False)
    usuario = models.OneToOneField(User, related_name="apicultor", on_delete = models.CASCADE)

    def __str__(self):
        return self.nome
    
    
class Apiario(models.Model):
    qtd_colmeias = models.IntegerField()
    apicultor = models.ForeignKey('Apicultor', on_delete=models.CASCADE, related_name="apiarios")
    localizacao = models.CharField(max_length=255, null=False)
    

    def __str__(self):
        return 'Api '+ str(self.id) + ' - ' + str(self.apicultor)
    
    def excluir_apiario(self):
        self.delete() 

   
class CaixaRacional(models.Model):
    apiario = models.ForeignKey('Apiario', on_delete=models.CASCADE, related_name="caixas_racionais")
    identificador = models.CharField(max_length=255, null=False)
    especie = models.CharField(max_length=255, null=False)
   
    def excluir_caixa_racional(self):
        self.delete() 
    

class Perda(models.Model):
    TIPO_PERDA_CHOICES = (
        ('MORTE POR ABANDONO', 'Morte por abandono'),
        ('MORTE POR AGROTÓXICO', 'Morte por agrotóxico'),
    )
    
    tipo_perda = models.CharField(max_length=20, choices=TIPO_PERDA_CHOICES, null=False, blank=False)
    qtd_colmeias_perdidas = models.IntegerField()
    data_registro_perda = models.DateTimeField(auto_now_add=True)
    especie_perdida = models.CharField(max_length=255, null=False)
    #foto_perda = models.FileField(required=False)
    apiario = models.ForeignKey('Apiario', on_delete=models.CASCADE, related_name="perdas")

    class Meta:
        ordering = ['-data_registro_perda']

    def excluir_perda(self):
        self.delete()