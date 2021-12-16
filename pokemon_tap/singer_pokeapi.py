import singer
import requests

endpoint = "https://pokeapi.co/"
route = "api/v2/pokemon/"

def retrieve_pokemons():
  authenticated_endpoint = "{}{}?offset=20&limit=130".format(endpoint, route)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response['results']

def retrieve_pokemon_details(id):
  authenticated_endpoint = "{}{}/{}".format(endpoint, route, id)
  # print(authenticated_endpoint)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response

poke_items = retrieve_pokemons()

schema = {'properties': {
    'name': {'type': 'string'},
    'url': {'type': 'string'},
    'weight': {'type': 'integer'},
    'height': {'type': 'integer'}
    }
  }
singer.write_schema(stream_name="pokemon_details", schema=schema, key_properties=[])
# Write a single record to the stream, that adheres to the schema
# singer.write_record(stream_name="pokemons",  record={**poke_items[0], "name": "bulbamon"})
i=20
for pokemon in poke_items:
  i+=1
  details = retrieve_pokemon_details(i)
  singer.write_record(stream_name="pokemon_details",  record={**pokemon, "index": i, 'weight': details['weight'], 'height': details['height']})