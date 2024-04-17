
import json
import mysql.connector
import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()
aim_network = None
for network in networks:
    if network.name == 'monitoring_network':
        aim_network = network
        break

print(aim_network)
print(aim_network.name)
print(aim_network.containers)

# If the network was found, print the names of all containers in it
if ai is not None:
    for container in client.containers:
        print(container.name)
else:
    print("Network 'monitoring_network' not found")

