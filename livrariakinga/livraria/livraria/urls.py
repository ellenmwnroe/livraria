# livraria/urls.py
from django.contrib import admin
from django.urls import path, include  # Inclui as URLs de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),  # Inclui as URLs do app 'livros'
]
