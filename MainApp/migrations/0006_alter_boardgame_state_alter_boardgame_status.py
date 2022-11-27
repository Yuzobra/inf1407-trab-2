# Generated by Django 4.1.3 on 2022-11-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_alter_boardgame_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='state',
            field=models.CharField(choices=[('Novo', 'Novo'), ('USADO', 'Usado'), ('DEGRADADO', 'Degradado')], max_length=9),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='status',
            field=models.CharField(choices=[('DISPONIVEL', 'Disponivel'), ('VENDIDO', 'Vendido')], default='AVAILABLE', max_length=10),
        ),
    ]
