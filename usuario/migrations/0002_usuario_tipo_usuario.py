# Generated by Django 5.0.6 on 2024-06-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.IntegerField(choices=[(1, 'Cliente'), (2, 'Vendedor'), (3, 'Gerente')], default=1, verbose_name='User Type'),
        ),
    ]
