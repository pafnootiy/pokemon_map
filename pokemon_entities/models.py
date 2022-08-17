from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="pokemon_pic")
    description = models.TextField(null=True, blank=True)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name="next_evolutions")

    def __str__(self):
        return '{}'.format(self.title)


#
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(blank=True, verbose_name="Долгота")
    longitude = models.FloatField(blank=True, verbose_name="Широта")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появляется до")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Исчезает в")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень")
    Defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    Health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье")
    Strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    Stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость")
