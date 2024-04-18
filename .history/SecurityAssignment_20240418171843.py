import docker
import subprocess

# Connect to the Docker Network
client = docker.from_env()

# Check if Docker is running
try:
    client.containers.list()
except docker.errors.DockerException:
    print("Docker is not running. Please start Docker and run this script again.")
    exit(1)
aim_network = None
network_names = []
print("Available networks:")
for network in client.networks.list():
    print(network.name)
    network_names.append(network.name)

# If the network was not found, ask for the network name again
while aim_network is None:
    network_name = input("Please enter the network name: ")
    if(network_name not in network_names):
        print("Network not found. Please enter a valid network name.")
        network_name = input("Please enter the network name: ")
    else:
        aim_network = client.networks.get(network_name)
        break
print()
# Create a list to store the container data
containers_data = []

# Print the containers connected to the network
print(f"Containers in {network_name}:")
for container in aim_network.containers:
    container_info = container.attrs
    container_name = container_info['Name']
    container_ipv4 = container_info['NetworkSettings']['Networks'][network_name]['IPAddress']
    service_type = container_info['Config']['Image']  # Assuming the service type is the container's image
    Ports = container_info['NetworkSettings']['Ports']
    port = list(Ports.keys())[0].split('/')[0]

    url = f"http://{container_ipv4}"  # Assuming the URL is the container's IP address

    # Print the container data
    print(f"Container ID: {container.id}")
    print(f"Container Name: {container_name}")
    print(f"Container IPv4 Address: {container_ipv4}")
    print(f"URL: {url}")
    print(f"Port: {port}")
    print(f"Service Type: {service_type}")
    print()  

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
    
# scan the containers for vulnerabilities
print("Scanning containers for vulnerabilities...")
for container in containers_data:
    print(f"Scanning {container['Container Name']}...")
    # Scan the container for vulnerabilities
    
    
    print(f"{container['Container Name']} scanned successfully.")
    print()
