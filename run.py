import os
from v2tj import convert_uri_json

# Read URIs from file
with open('uris.txt', 'r') as f:
    uris = f.read().split(',')

# Loop through all URIs
for uri in uris:
    file = convert_uri_json(uri=uri.strip())
