# Generated by Django 5.0.2 on 2024-03-25 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0003_alter_actividadevaluativa_objetivoevaluar_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clase',
            unique_together={('asignatura', 'numero')},
        ),
    ]
