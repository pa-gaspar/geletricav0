# Generated by Django 2.2.4 on 2019-10-31 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('potenciaProjeto', models.IntegerField(blank=True, null=True)),
                ('sinalAlerta', models.BooleanField(default=False)),
                ('chaveArea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bancoDeDados.area')),
            ],
        ),
        migrations.CreateModel(
            name='cargaTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=300)),
                ('potenciaProjeto', models.IntegerField(blank=True, null=True)),
                ('tensaoCircuitoLuminaria', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('correnteCircuitoLuminaria', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('potenciaCircuitoLuminaria', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sinalAlerta', models.BooleanField(default=False)),
                ('chaveLocal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancoDeDados.area')),
            ],
        ),
        migrations.CreateModel(
            name='carga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=300)),
                ('potencia', models.IntegerField()),
                ('notas', models.CharField(blank=True, max_length=300, null=True)),
                ('tempoUsoDiario', models.FloatField(blank=True, null=True)),
                ('mediaConsumo', models.IntegerField(blank=True, null=True)),
                ('xPosicao', models.IntegerField(blank=True, null=True)),
                ('yPosicao', models.IntegerField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='geletrica_data/pictures/')),
                ('sinalAlerta', models.BooleanField(default=False)),
                ('chaveCarga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bancoDeDados.local')),
            ],
        ),
    ]
