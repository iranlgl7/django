# Generated by Django 5.0.2 on 2024-04-04 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eva', '0016_respuestaduda_resuelta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaduda',
            name='resuelta',
        ),
    ]