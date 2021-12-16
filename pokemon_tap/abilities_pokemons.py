import singer
import requests

endpoint = "https://pokeapi.co/"
route = "api/v2/pokemon/"

def retrieve_pokemon_abilities(id):
  authenticated_endpoint = "{}{}/{}".format(endpoint, route, id)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["abilities"]

schema = {'properties': {
    'index': {'type': 'integer'},
    'ability': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="pokemon_abilities", schema=schema, key_properties=[])
# Write a single record to the stream, that adheres to the schema
# singer.write_record(stream_name="pokemons",  record={**poke_items[0], "name": "bulbamon"})
list = range(130)
j=20
for i in list:
  j+=1
  abilities = retrieve_pokemon_abilities(j)
  for ability in abilities:
    singer.write_record(stream_name="pokemon_abilities",  record={"index": j, 'ability': ability["ability"]["name"]})