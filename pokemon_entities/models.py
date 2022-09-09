from django.db import models



class Pokemon(models.Model):


    title = models.CharField(max_length=200, verbose_name="Название покемона")
    picture = models.ImageField(upload_to="pokemon_pic", verbose_name="Картинка")
    description = models.TextField(blank=True, verbose_name="Описание")
    title_en = models.CharField(max_length=200,blank=True,verbose_name="Название покемона, англ.")
    title_jp = models.CharField(max_length=200,blank=True, verbose_name="Название покемона, яп.")
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name="next_evolutions", verbose_name="Предыдущая эволюция")



    def __str__(self):
        return self.title



class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True,related_name="pokemon_entities",verbose_name='Покемон')
    latitude = models.FloatField(verbose_name="Долгота")
    longitude = models.FloatField(verbose_name="Широта")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появляется до")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Исчезает в")
    level = models.IntegerField(blank=True, verbose_name="Уровень")
    defence = models.IntegerField(blank=True, verbose_name="Защита")
    health = models.IntegerField(blank=True, verbose_name="Здоровье")
    strength = models.IntegerField(blank=True, verbose_name="Сила")
    stamina = models.IntegerField(blank=True, verbose_name="Выносливость")
