# Generated by Django 2.1.3 on 2018-11-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0003_auto_20181102_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='paquete',
            field=models.ManyToManyField(through='entrega.Asignacion', to='entrega.Paquete'),
        ),
    ]
