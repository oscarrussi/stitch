import singer
import requests

def retrieve_pokemons():
  endpoint = "https://pokeapi.co/"
  route = "api/v2/pokemon/"
  authenticated_endpoint = "{}{}".format(endpoint, route)
  api_response = requests.get(authenticated_endpoint).json()
  return api_response['results']


poke_items = retrieve_pokemons()

schema = {'properties': {
    'name': {'type': 'string'},
    'url': {'type': 'string'}
    }
  }
singer.write_schema(stream_name="pokemons", schema=schema, key_properties=[])

def main():
  for pokemon in poke_items:
    singer.write_record(stream_name="pokemons",  record={**pokemon})

if __name__ == "__main__":
    main()