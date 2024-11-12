from django.db import models

# Create your models here.
class Libros (models.Model):
    id_libros = models.CharField (max_length=10, blank=False, primary_key=True)
    nombre = models.CharField (max_length=50, blank=False)
    autor = models.CharField (max_length=50, blank=False)
    Fecha_creacion = models.DateField ()
    def __str__(self):
        return self.nombre
class Categorias (models.Model):
    id_categorias = models.CharField (max_length=10, blank=False, primary_key=True)
    nombre = models.CharField (max_length=50, blank=False)
    Descripcion = models.TextField ()
    def __str__(self):
        return self.nombre
    
class Ordenes (models.Model):
    id_ordenes = models.CharField (max_length=10, blank=False, primary_key=True)
    id_libros = models.ForeignKey (Libros, on_delete=models.RESTRICT)
    id_categorias = models.ForeignKey (Categorias, on_delete=models.RESTRICT)
    fecha_orden = models.DateTimeField (auto_now_add=True)
    descripcion = models.TextField()
    def __str__(self):
        return self.id_ordenes
    