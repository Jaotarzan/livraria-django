# Generated by Django 5.0.6 on 2024-06-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscompra',
            name='preco_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
