# Generated by Django 4.2.3 on 2023-10-22 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_persona_unique_together_persona_edad_mayor_18'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.persona')),
                ('empleo', models.CharField(max_length=50, verbose_name='Empleo')),
            ],
            bases=('home.persona',),
        ),
    ]