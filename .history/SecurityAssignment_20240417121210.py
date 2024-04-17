import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()
aim_network = None
for network in networks:
    if network.name == 'monitoring_network':
        aim_network = network
        break

container = client.containers.get('mysql')

# Check if the container is already connected to the network
if not any(c.name == 'mysql' for c in aim_network.containers):
    aim_network.connect(container)

print(aim_network)
print(aim_network.name)
print(aim_network.containers)


# If the network was found, print the names of all containers in it
if aim_network is not None:
    for container in aim_network.containers:
        print(container)
else:
    print("Network 'monitoring_network' not found")