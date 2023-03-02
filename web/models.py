from django.db import models
from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from categorias.models import Categoria

# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now, blank=True)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    def __str__(self):
        return self.titulo


