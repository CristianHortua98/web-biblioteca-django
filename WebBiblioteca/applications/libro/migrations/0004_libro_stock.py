# Generated by Django 4.2.3 on 2023-10-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_alter_libro_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]