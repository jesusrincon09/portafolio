from django.db import models

# Create your models here.
class About(models.Model):

    name = models.CharField(max_length=200,verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="about")

    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    

    class Meta:
        verbose_name = "Biografia"
        verbose_name_plural = "Biografias"
        ordering = ['-created']
    
    def __str__(self):
        return self.name