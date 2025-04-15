from django.db import models
from contas.models import func_usuarios
# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    professor = models.ForeignKey(func_usuarios, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nome
    
class Desempenho(models.Model):
    aluno = models.ForeignKey(func_usuarios, on_delete=models.CASCADE, related_name='desempenhos')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='desempenhos')
    nota = models.FloatField()
    

    def __str__(self):
        return f"{self.aluno.username} - {self.curso.nome} - {self.nota}"