from django.db import models

class Presentacion(models.Model):

    titulo = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.titulo

class Diapositivas(models.Model):

    presentacion = models.ForeignKey(Presentacion,related_name="diapositivas")
    contenido = models.TextField()
