from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    objects = None
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField(blank=False, null=False)
    data_publicacao = models.DateTimeField(default=timezone.now)

    # Função para exibir na tela o titulo.
    def __str__(self):
        return self.titulo
