# Generated by Django 5.0.2 on 2024-04-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0012_alter_duda_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duda',
            name='estado',
        ),
        migrations.AddField(
            model_name='duda',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
