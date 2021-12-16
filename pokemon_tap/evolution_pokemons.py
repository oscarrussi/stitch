import singer
import requests

endpoint = "https://pokeapi.co/"
route = "api/v2/evolution-chain/"

def retrieve_pokemon_abilities(id):
  authenticated_endpoint = "{}{}/{}".format(endpoint, route, id)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response["chain"]

schema = {'properties': {
    'evolves_from': {'type': 'string'},
    'evolves_to': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="pokemon_evolutions", schema=schema, key_properties=[])
# Write a single record to the stream, that adheres to the schema
# singer.write_record(stream_name="pokemons",  record={**poke_items[0], "name": "bulbamon"})
list = range(50)
for i in list:
  i+=7
  evolutions = retrieve_pokemon_abilities(i)
  singer.write_record(stream_name="pokemon_evolutions",  record={"evolves_from": evolutions["species"]["name"], 'evolves_to': evolutions["evolves_to"][0]["species"]["name"]})
  if len(evolutions["evolves_to"][0]["evolves_to"])>0:
    singer.write_record(stream_name="pokemon_evolutions",  record={"evolves_from": evolutions["evolves_to"][0]["species"]["name"], 'evolves_to': evolutions["evolves_to"][0]["evolves_to"][0]["species"]["name"]})