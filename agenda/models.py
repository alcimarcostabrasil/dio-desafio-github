from django.db import models
from stdimage import StdImageField


class Agenda(models.Model):
    foto = StdImageField(upload_to='imagem/contato',
                         variations={'thumbnail': {'width': 100, 'height': 100}})
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    telefone = models.CharField(max_length=15, null=False, blank=False, verbose_name='Telefone')

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        db_table = 'agendas'

    def __str__(self):
        return self.nome
