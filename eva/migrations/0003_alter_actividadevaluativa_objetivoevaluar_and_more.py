# Generated by Django 5.0.2 on 2024-03-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0002_remove_actividadevaluativa_objetivo_evaluar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadevaluativa',
            name='objetivoEvaluar',
            field=models.TextField(blank=0, null=0),
        ),
        migrations.AlterField(
            model_name='clase',
            name='encabezado',
            field=models.TextField(blank=0, null=0),
        ),
    ]
