# Generated by Django 2.2.4 on 2019-11-16 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancoDeDados', '0002_carga_tipodacarga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carga',
            name='tipoDaCarga',
        ),
    ]
