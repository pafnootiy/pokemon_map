# Generated by Django 4.0.6 on 2022-07-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
