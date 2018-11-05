# Generated by Django 2.1.3 on 2018-11-03 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=60)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Camionero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50)),
                ('salario', models.CharField(max_length=60)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrega.Camion')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
    ]
