import os
import json

# Directory containing the JSON files
directory = 'configs'

# List to store the contents of all JSON files
combined = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        # Full file path
        filepath = os.path.join(directory, filename)

        # Open and read the JSON file
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Add the content to the combined list
        combined.append(data)

# Write the combined content to a new JSON file
with open('configs/combined.json', 'w') as f:
    f.write('[\n')
    for item in combined:
        f.write('    ' + json.dumps(item, indent=4).replace('\n', '\n    ') + ',\n')
    f.write(']\n')
