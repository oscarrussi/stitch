import singer
import requests

endpoint = "https://pokeapi.co/"
route = "api/v2/evolution-chain/"

def retrieve_pokemon_chain(id):
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

def add_evolutions(pokemon_name, evols):
  for evol in evols:
    singer.write_record(stream_name="pokemon_evolutions",  record={"evolves_from": pokemon_name, 'evolves_to': evol["species"]["name"]})
    if len(evol["evolves_to"])>0:
      add_evolutions(evol["species"]["name"], evol["evolves_to"])


list = range(77)
for i in list:
  i+=1
  evolutions = retrieve_pokemon_chain(i)
  if len(evolutions["evolves_to"])>0:
    add_evolutions(evolutions["species"]["name"], evolutions["evolves_to"])


