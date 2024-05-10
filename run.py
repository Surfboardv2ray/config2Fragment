import os
from v2tj import convert_uri_json
import base64


def get_remarks(uri):
    """Extracts remarks from the provided V2Ray URI.

    Args:
        uri (str): The V2Ray URI string.

    Returns:
        str: The extracted remarks with '+Fragment' appended, or None if not found.
    """

    if uri.startswith("vmess://"):
        # Decode base64-encoded vmess URI
        try:
            decoded_uri = base64.b64decode(uri[8:]).decode()
        except Exception as e:
            print(f"Error decoding vmess URI: {uri}. Error: {str(e)}")
            return None

        # Extract remarks from "ps" attribute in decoded JSON
        import json  # Import json only when needed
        try:
            data = json.loads(decoded_uri)
            remarks = data.get("ps")
            return remarks + '+Fragment' if remarks else None
        except json.JSONDecodeError as e:
            print(f"Error parsing decoded vmess URI: {uri}. Error: {str(e)}")
            return None

    elif uri.startswith("vless://") or uri.startswith("trojan://"):
        # Split URI to extract remarks after "#"
        parts = uri.split("#", 1)
        remarks = parts[1] if len(parts) > 1 else None
        return remarks + '+Fragment' if remarks else None

    else:
        return None


def convert_uri_json_with_remarks(uri):
    """Converts V2Ray URI to JSON, incorporating remarks with '+Fragment'.

    Args:
        uri (str): The V2Ray URI string.

    Returns:
        dict: The converted JSON data with added remarks, or None on error.
    """

    try:
        # Print the output of v2tj to see if conversion works initially
        print(f"Converting URI: {uri}")
        json_data = convert_uri_json(uri)
        print(f"v2tj output: {json_data}")  # Remove this line after debugging

        remarks = get_remarks(uri)

        if remarks:
            # Insert remarks one line above "log" with proper indentation
            log_index = next(i for i, item in enumerate(json_data) if item["key"] == "log")
            json_data.insert(log_index, {"key": "remarks", "value": remarks})

        return json_data
    except Exception as e:
        print(f"Cannot parse URI: {uri}. Error: {str(e)}")
        return None


# Read URIs from file
with open('uris.txt', 'r') as f:
    uris = f.read().split(',')

# Loop through all URIs
for uri in uris:
    try:
        json_data = convert_uri_json_with_remarks(uri.strip())
        if json_data:
            # Save converted JSON with remarks
            filename = os.path.join("configs", os.path.basename(uri.strip()) + ".json")
            with open(filename, 'w') as f:
                import json  # Import json only when needed
                json.dump(json_data, f, indent=4)  # Use consistent indentation

    except Exception as e:
        print(f"Error processing URI: {uri.strip()}. Error: {str(e)}")
