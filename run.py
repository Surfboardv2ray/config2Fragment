import os
from v2tj import convert_uri_json

uri = os.getenv('URI_SECRET')
file = convert_uri_json(uri=uri)
