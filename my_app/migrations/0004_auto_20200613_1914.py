# Generated by Django 3.0.7 on 2020-06-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200613_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='comentario',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Comentarios'),
        ),
    ]
