import requests
import pprint

endpoint = "https://pokeapi.co/"

# Fill in the correct API key
route = "api/v2/pokemon/"

# Create the web API’s URL
authenticated_endpoint = "{}{}".format(endpoint, route)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response['results'])