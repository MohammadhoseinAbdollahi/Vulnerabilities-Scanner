import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()
aim_network = None

# Find the monitoring_network
for network in networks:
    if network.name == 'monitoring_network':
        aim_network = network
        break

# If the network was found, print the names of all containers in it
if aim_network is not None:
    # Print the containers connected to the network
    print("Containers in monitoring_network:")
    for container_id, container_info in aim_network.attrs['Containers'].items():
        container_name = client.containers.get(container_id).name
        container_ipv4 = container_info['IPv4Address'].split('/')[0]  # Remove the CIDR suffix
        print(f"Container ID: {container_id}")
        print(f"Container Name: {container_name}")
        print(f"Container IPv4 Address: {container_ipv4}")
        print()  # Add a blank line for readability
else:
    print("Network 'monitoring_network' not found")
