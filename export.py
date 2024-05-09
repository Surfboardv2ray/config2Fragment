import os
import json
from v2tj import convert_uri_json

# Directory containing the JSON files
directory = 'configs'

# List to store the contents of all JSON files
combined = []

# Loop through all URIs
for uri in uris:
    file = convert_uri_json(uri=uri.strip())

# Write the combined content to a new JSON file
with open('configs/combined.json', 'w') as f:
    f.write('[\n')
    for i, item in enumerate(combined):
        # If this is the last item, don't add a comma after it
        if i == len(combined) - 1:
            f.write('    ' + json.dumps(item, indent=4).replace('\n', '\n    ') + '\n')
        else:
            f.write('    ' + json.dumps(item, indent=4).replace('\n', '\n    ') + ',\n')
    f.write(']\n')
