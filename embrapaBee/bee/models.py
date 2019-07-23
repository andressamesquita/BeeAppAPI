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

    @property
    def get_perdas(self):
        return Perda.objects.filter(id=self.id)
   
class Apiario(models.Model):
    TIPO_CHOICES = (
        ('MELIPONARIO', 'Meliponário'),
        ('APIÁRIO', 'Apiário'),
    )
    
    tipo = models.CharField(max_length=11, choices=TIPO_CHOICES, null=False, blank=False)
    qtd_colmeias = models.IntegerField()
    apicultor = models.ForeignKey('Apicultor', on_delete=models.CASCADE, related_name="apiarios")
    localizacao = models.CharField(max_length=255, null=False)
    

    def __str__(self):
        return str(self.tipo) + '  ' + str(self.id) + ' - ' + str(self.apicultor) 
    
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
    apiario = models.ForeignKey('Apiario', on_delete=models.CASCADE, related_name="perdas")

    foto_perda = models.ImageField(upload_to='fotos_perdas', null=True, blank = True)

    class Meta:
        ordering = ['-data_registro_perda']

    def excluir_perda(self):
        self.delete()

class Racao(models.Model):
    INGREDIENTE_CHOICES = (
        ('SOJA', 'soja'),
        ('FUBA', 'fuba'),
        ('MANDIOCA', 'mandioca'),
        ('BABAÇU', 'babaçu'),
        ('LEUCENA', 'leucena'),
        ('PURILAC', 'purilac'),
        ('ALGAROBA', 'algaroba'), 
    )

    ingrediente_1 = models.CharField(max_length=12, choices=INGREDIENTE_CHOICES, null=False, blank=False)
    ingrediente_2 = models.CharField(max_length=12, choices=INGREDIENTE_CHOICES, null=False, blank=False)
    pb_ingr_1 = models.FloatField(null=True, blank=True, default=None)
    pb_ingr_2 = models.FloatField(null=True, blank=True, default=None)

    def fazer_calculo_balanceamento_racao(self):
        
        porc_bruta_racao = 20

        if (self.pb_ingr_1 > porc_bruta_racao):
            dif_pb1 = self.pb_ingr_1 - porc_bruta_racao   
        else:
            dif_pb1 = porc_bruta_racao - self.pb_ingr_1 

        if (self.pb_ingr_2 > porc_bruta_racao):
            dif_pb2 = self.pb_ingr_2 - porc_bruta_racao
        else:
            dif_pb2 = porc_bruta_racao - self.pb_ingr_2

        total_porcentagem = dif_pb1 + dif_pb2

        calc_ing_1 = (dif_pb1 * 100)/total_porcentagem
        calc_ing_2 = 100 - calc_ing_1

        return str(self.ingrediente_1) + ': ' + calc_ing_1 + ' | ' + str(self.ingrediente_2) + ': ' + calc_ing_2 