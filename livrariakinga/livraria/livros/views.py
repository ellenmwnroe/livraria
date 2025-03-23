# livros/views.py
from django.shortcuts import render
from .models import Livro
from django.http import HttpResponse

# Página inicial da livraria
def index(request):
    return HttpResponse("Bem-vindo à Livraria!")

# Lista de livros
def lista_livros(request):
    livros = Livro.objects.all()  # Recupera todos os livros do banco de dados
    return render(request, 'livros/lista_livros.html', {'livros': livros})
