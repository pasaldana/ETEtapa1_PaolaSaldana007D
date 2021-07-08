from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre del registro')

    def __str__(self):
        return(self.nombreCategoria)

class Registro(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut del colaborador')
    foto = models.CharField(max_length=1,verbose_name='Fotografía que lo identifique')   
    nombre = models.CharField(max_length=50, verbose_name='Nombre completo')
    telefono = models.CharField(max_length=9, verbose_name='Telefóno')    
    direccion = models.CharField(max_length=50, verbose_name='Dirección')    
    email = models.CharField(max_length=50, verbose_name='E-mail')
    pais = models.CharField(max_length=15,verbose_name='País')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)    

    def __str__(self):
        return(self.rut)