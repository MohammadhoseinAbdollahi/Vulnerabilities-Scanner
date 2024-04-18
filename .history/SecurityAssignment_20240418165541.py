import docker
import json

# Connect to the Docker Network
client = docker.from_env()

# Check if Docker is running
try:
    client.containers.list()
except docker.errors.DockerException:
    print("Docker is not running. Please start Docker and run this script again.")
    exit(1)



# If the network was not found, ask for the network name again
while aim_network is None:
    network_name = input("Please enter the network name: ")
    if(network_name != client.networks.get(network_name)):
        print("Network not found. Please enter a valid network name.")
        network_name = input("Please enter the network name: ")
    print(f"Network '{network_name}' not found.")
    aim_network = client.networks.get(network_name)

# Create a list to store the container data
containers_data = []

# Print the containers connected to the network
print(f"Containers in {network_name}:")
for container in aim_network.containers:
    container_info = container.attrs
    container_name = container_info['Name']
    container_ipv4 = container_info['NetworkSettings']['Networks'][network_name]['IPAddress']
    url = f"http://{container_ipv4}"  # Assuming the URL is the container's IP address

   

    print(f"Container ID: {container.id}")
    print(f"Container Name: {container_name}")
    print(f"Container IPv4 Address: {container_ipv4}")
    print(f"URL: {url}")
    print(f"Port: {port}")
    print(f"Service Type: {service_type}")
    print()  # Add a blank line for readability

        # Create a dictionary with the data
    data = {
            "Container Name": container_name,
            "Container IPv4 Address": container_ipv4,
            "URL": url,
            "Port": port,
            "Service Type": service_type
        }

    # Add the dictionary to the list
    containers_data.append(data)

else:
    print("Network 'monitoring_network' not found")
    
# Print the list of container data
print(containers_data)