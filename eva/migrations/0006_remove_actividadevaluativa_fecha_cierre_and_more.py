# Generated by Django 5.0.2 on 2024-04-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0005_alter_actividadevaluativa_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividadevaluativa',
            name='fecha_cierre',
        ),
        migrations.AddField(
            model_name='actividadevaluativa',
            name='habilitada',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='estudiantes',
            field=models.ManyToManyField(blank=1, to='eva.estudiante'),
        ),
    ]
