from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='categorias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.titulo

