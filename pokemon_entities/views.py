import folium


from contextlib import suppress
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=localtime(),
        disappeared_at__gt=localtime()
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.picture.url),
        )

    pokemons_on_page = []

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.picture.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    pokemon_entities = pokemon.entities.all()

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.picture.url,
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp}

    if pokemon.previous_evolution:
        pokemon_data['previous_evolution'] = {
            'pokemon_id': pokemon.previous_evolution.id,
            'img_url': pokemon.previous_evolution.picture.url,
            'title_ru': pokemon.previous_evolution.title
        }

    with suppress(IndexError, ObjectDoesNotExist):
        next_evolution = pokemon.next_evolutions.get()
        if next_evolution:
            pokemon_data['next_evolution'] = {
                'pokemon_id': next_evolution.id,
                'img_url': next_evolution.picture.url,
                'title_ru': next_evolution.title
            }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data,
    })
