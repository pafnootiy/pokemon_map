# Generated by Django 4.0.6 on 2022-07-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_pokemonentity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PokemonEntity',
        ),
    ]
