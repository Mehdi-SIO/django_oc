#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect


def home(request):
    """Exemple de page html non valide"""
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)
# Create your views here.

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    #SI l'ID de l'article est supérieur à 100, on cosidère qu'il n'existe pas
    if int(id_article) > 100:
        raise Http404

    return HttpResponse(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé")

def list_articles(request, year, month):
    #Redirection vers un site web
    return redirect("https://www.djangoproject.com")