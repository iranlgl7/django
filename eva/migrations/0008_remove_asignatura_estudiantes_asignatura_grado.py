# Generated by Django 5.0.2 on 2024-04-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0007_remove_actividadevaluativa_habilitada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='estudiantes',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='grado',
            field=models.PositiveIntegerField(blank=0, default=7, null=0),
            preserve_default=False,
        ),
    ]
