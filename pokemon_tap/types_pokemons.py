import singer
import requests

endpoint = "https://pokeapi.co/"
route = "api/v2/pokemon/"

def retrieve_pokemon_types(id):
  authenticated_endpoint = "{}{}/{}".format(endpoint, route, id)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["types"]

schema = {'properties': {
    'index': {'type': 'integer'},
    'type': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="pokemon_types", schema=schema, key_properties=[])
# Write a single record to the stream, that adheres to the schema
# singer.write_record(stream_name="pokemons",  record={**poke_items[0], "name": "bulbamon"})
list = range(130)
j=20
for i in list:
  j+=1
  types = retrieve_pokemon_types(j)
  for type in types:
    singer.write_record(stream_name="pokemon_types",  record={"index": j, 'type': type["type"]["name"]})