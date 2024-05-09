# Read URIs from subs.txt
with open('list.txt', 'r') as f:
    uris = f.read().splitlines()

# Write URIs to uris.txt
with open('uris.txt', 'w') as f:
    f.write(','.join(uris))
