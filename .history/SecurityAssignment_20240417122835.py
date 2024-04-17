import docker

# Connect to the Docker Network
client = docker.from_env()

# Find the monitoring_network
aim_network = client.networks.get('monitoring_network')
# If the network was found, print the names of all containers in it
if aim_network is not None:
    # Print the containers connected to the network
    print("Containers in monitoring_network:")
    for container in aim_network.containers:
        container_info = container.attrs
        # container_name = container_info['Name']
        # container_ipv4 = container_info['NetworkSettings']['Networks']['monitoring_network']['IPAddress']
        # print(f"Container ID: {container.id}")
        # print(f"Container Name: {container_name}")
        # print(f"Container IPv4 Address: {container_ipv4}")
        # print()  # Add a blank line for readability
else:
    print("Network 'monitoring_network' not found")
