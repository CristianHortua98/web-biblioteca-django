# Generated by Django 4.2.3 on 2023-10-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
    ]
