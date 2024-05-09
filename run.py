import json
from v2tj import convert_uri_json  # Assuming v2tj is in the same directory or on your path

def convert_uri_to_json(uri):
    # Your V2Ray to JSON conversion logic goes here (using v2tj)

uris = sys.argv[1:]  # Get all arguments after script name (list of URIs)

for uri in uris:
    converted_json = convert_uri_to_json(uri=uri)
    # No need to modify the converted JSON as v2tj should handle it

# v2tj presumably saves the JSON to /configs already, so no additional saving logic here
