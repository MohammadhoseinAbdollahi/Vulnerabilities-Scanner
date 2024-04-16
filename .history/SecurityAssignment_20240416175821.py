import requests
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
container = client.containers.get('your_container_id')
container.connect(network=aim_network.id)

