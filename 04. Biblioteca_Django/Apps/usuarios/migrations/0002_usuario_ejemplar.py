# Generated by Django 4.2.1 on 2023-05-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_autor_libro'),
        ('prestamos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ejemplar',
            field=models.ManyToManyField(through='prestamos.Prestar', to='biblioteca.ejemplar', verbose_name='prestar'),
        ),
    ]