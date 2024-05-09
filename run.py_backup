import os
from v2tj import convert_uri_json

uris = os.getenv('URIS').split(',')
for uri in uris:
    file = convert_uri_json(uri=uri.strip())
