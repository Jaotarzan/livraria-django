from django.contrib import admin

from .models import Autor, Categoria, Editora, Livro

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Editora)