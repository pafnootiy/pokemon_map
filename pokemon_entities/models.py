from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(null=True,blank=True)
    Defence = models.IntegerField(null=True,blank=True)
    Health = models.IntegerField(null=True,blank=True)
    Strength = models.IntegerField(null=True,blank=True)
    Stamina = models.IntegerField(null=True,blank=True)

