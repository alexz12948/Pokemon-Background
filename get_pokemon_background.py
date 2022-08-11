#!/usr/bin/env python3
'''
Name: Alexander Zsikla
Last Updated: August 11, 2022
get_pokemon_background.py

Updates the background of the main desktop to have a random pokemon sprite
'''

import requests
import os
from random import randint

# UPDATE THIS LINE WITH WHERE THE SCRIPT RESIDES FOR YOU
FILENAME = "/Users/alexanderzsikla/code/tufts-cs/coding101/demo-automation/pokemon.png"
url = "https://pokeapi.co/api/v2/pokemon/"

def get_random_pokemon():
  '''
  get_random_pokemon

  Randomly gets a pokemon's image from the pokemon API
  '''
  pokemon_id = randint(1, 493)
  r = requests.get(f'{url}/{pokemon_id}')

  if r.status_code != 200:
    print(f"Couldn't get pokemon with id {pokemon_id}")
    return
  
  sprite_url = r.json()['sprites']['front_default']
  sprite = requests.get(sprite_url, allow_redirects=True)

  open(FILENAME, 'wb').write(sprite.content)

if __name__ == "__main__":
  get_random_pokemon()
  os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + FILENAME +"\"'")
  os.system("killall Dock")
