# Generated by Django 5.0.2 on 2024-04-03 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0008_remove_asignatura_estudiantes_asignatura_grado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaactividadevaluativa',
            name='estado',
        ),
    ]