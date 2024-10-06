from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(verbose_name = "Título",max_length=255)
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url = models.URLField(verbose_name="Dirección web", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True) # Se crea la fecha solo una vez, cuando se crea
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True) # se actualiza cada vez q se actualice
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # El más antiguo al más nuevo
    
    def __str__(self):
        return self.title