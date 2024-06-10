# Generated by Django 5.0.6 on 2024-06-10 12:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livraria', '0001_initial'),
        ('uploader', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itenscompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='livraria.compra'),
        ),
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='livraria.autor'),
        ),
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.categoria'),
        ),
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.editora'),
        ),
        migrations.AddField(
            model_name='itenscompra',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='livraria.livro'),
        ),
    ]
