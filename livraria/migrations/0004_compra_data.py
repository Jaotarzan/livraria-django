# Generated by Django 5.0.6 on 2024-06-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_itenscompra_preco_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
