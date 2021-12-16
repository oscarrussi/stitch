endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{enpoint}/{api_key}".format(enpoint=endpoint, api_key=api_key)
print(authenticated_endpoint)