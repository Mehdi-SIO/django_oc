from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

def __str__(self):
    """
    Cette methode que nous definirons dans tous les modeles
    nous permettra de reconnaitre facilement les differents objets que
    nous traiterons plus tard et dans l'administration
    """

    return self.titre
