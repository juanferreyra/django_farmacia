# Generated by Django 2.0.1 on 2018-01-20 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposito',
            name='fecha_modificacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
