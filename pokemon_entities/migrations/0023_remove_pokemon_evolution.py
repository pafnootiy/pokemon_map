# Generated by Django 4.0.6 on 2022-08-04 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0022_alter_pokemon_evolve_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='previous_evolution',
        ),
    ]
