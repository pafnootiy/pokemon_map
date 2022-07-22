from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()

