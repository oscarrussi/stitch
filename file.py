# # Import json
# import json

# database_address = {
#   "host": "10.0.0.5",
#   "port": 8456
# }

# # Open the configuration file in writable mode
# with open("database_config.json", "w") as fh:
#   # Serialize the object in this file handle
#   json.dump(obj=database_address, fp=fh) 

import json

database_address = {
  "host": "10.0.0.5",
  "port": 8456
}

print(json.dumps(database_address))
print(database_address)
