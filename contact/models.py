from django.db import models

# Create your models here.
class Contact(models.Model):

    description = models.TextField(verbose_name="Descripción")
    email = models.EmailField(verbose_name="correo")
    phone = models.PositiveIntegerField(verbose_name="Telefono")
    whatsapp = models.PositiveIntegerField(verbose_name="whatsapp")

    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-created']
    
    def __str__(self):
        return self.email