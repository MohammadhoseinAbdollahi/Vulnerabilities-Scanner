import requests
import json
import mysql.connector
import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()

