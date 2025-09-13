from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=2, default='BR')
    
    def __str__(self):
        return f"{self.nome}, {self.pais}"
    
class ConsultaTempo(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    temperatura = models.DecimalField(max_digits= 5, decimal_places=2)
    descricao = models.CharField(max_length=200, default='')
    umidade = models.IntegerField()
    data_consulta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cidade} - {self.temperatura}°C - {self.data_consulta}"