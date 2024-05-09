import sys
from v2tj import convert_uri_json

print('Arguments:', sys.argv)

uri = sys.argv[1]
file = convert_uri_json(uri=uri)
