import docker
import json

# Connect to the Docker Network
client = docker.from_env()

# Ask for the name of the network
network_name = input("Enter the name of the network: ")

# Check if the network exists
if network_name in [network.name for network in client.networks.list()]:
    # Continue with the rest of the code
    aim_network = client.networks.get(network_name)
    containers_data = []
    # Rest of the code...
else:

    print(f"Network '{network_name}' not found")
    print("Network 'monitoring_network' not found")