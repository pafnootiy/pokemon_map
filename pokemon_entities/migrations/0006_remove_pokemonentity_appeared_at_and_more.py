# Generated by Django 4.0.6 on 2022-07-22 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonentity',
            name='appeared_at',
        ),
        migrations.RemoveField(
            model_name='pokemonentity',
            name='disappeared_at',
        ),
    ]
