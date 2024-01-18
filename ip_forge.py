import uuid
import ipaddress
import random
import requests

def generate_browser_id_with_ipv4():
    # Generate a random UUID (Universally Unique Identifier)
    browser_id = str(uuid.uuid4())

    # Generate a random IPv4 address
    ipv4_address = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

    # Return the combination of UUID and IPv4 address
    return f"{browser_id}_{ipv4_address}"

# Example usage
random_browser_id_with_ipv4 = generate_browser_id_with_ipv4()
print("Generated UUID and IPv4 Address:", random_browser_id_with_ipv4)

# Extract UUID and IPv4 parts
uuid_part, ipv4_part = random_browser_id_with_ipv4.split('_')

# Use the extracted values
print("Extracted UUID:", uuid_part)
print("Extracted IPv4 Address:", ipv4_part)

# Make the API request for geolocation using the extracted IPv4 address
response = requests.post("http://ip-api.com/batch", json=[{"query": ipv4_part}]).json()

# Print the geolocation information
for ip_info in response:
    for k, v in ip_info.items():
        print(k, v)
    print('\n')
