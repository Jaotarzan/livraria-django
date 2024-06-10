from django.contrib import admin

from .models import Autor, Compra, Categoria, Editora, Livro



@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

admin.site.register(Compra)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('Nome',)
    search_fields = ('Nome',)
    list_filter = ('Nome',)
    ordering = ('Nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__Nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
