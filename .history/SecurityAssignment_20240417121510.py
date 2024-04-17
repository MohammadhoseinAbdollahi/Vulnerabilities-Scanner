import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()
aim_network = None
for network in networks:
    if network.name == 'monitoring_network':
        aim_network = network
        break

# If the network was found, print the names of all containers in it
if aim_network is not None:
    # Print the containers connected to the network
    print("Containers in monitoring_network:")
    for container_id, container_info in aim_network.containers.items():
        print("Container ID:", container_id)
        print("Container Name:", container_info['Name'])
        print("Container IPv4 Address:", container_info['IPv4Address'])
        print()  # Add a blank line for readability
else:
    print("Network 'monitoring_network' not found")
