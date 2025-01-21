import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.nome
    
@receiver(post_delete, sender=Pessoa)
def deletar_foto_pessoa(sender, instance, **kwargs):
    """Exclui a foto do diretório quando a Pessoa for deletada"""
    if instance.foto:  # Verifica se há uma foto salva
        if os.path.isfile(instance.foto.path):  # Verifica se o arquivo existe no sistema
            os.remove(instance.foto.path)  # Remove o arquivo
    
class Diario(models.Model):
    titulo = models.CharField(max_length=100)
    tags = models.TextField()
    pessoas = models.ManyToManyField(Pessoa, null=True, blank=True)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.titulo

    def get_tags(self):
        return self.tags.split(',') if self.tags else []
    
    def set_tags(self, list_tags, reset=False):
        if not reset:
            existing_tags = set(self.get_tags())
            list_tags = existing_tags.union(set(list_tags))

        self.tags = ','.join(list_tags)

