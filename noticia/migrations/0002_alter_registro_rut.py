# Generated by Django 3.2.4 on 2021-07-08 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut del colaborador'),
        ),
    ]