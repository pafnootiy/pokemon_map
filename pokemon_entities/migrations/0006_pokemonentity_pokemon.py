# Generated by Django 4.0.6 on 2022-07-22 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon'),
            preserve_default=False,
        ),
    ]
