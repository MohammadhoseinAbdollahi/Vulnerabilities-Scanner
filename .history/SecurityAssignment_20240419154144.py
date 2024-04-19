import docker
import subprocess
from docker.errors import DockerException  # Import specific exceptions


# Connect to the Docker Network


# Check if Docker is running
try:
    client = docker.from_env()
    containers = client.containers.list()
except docker.errors.DockerException:
    print("Docker is not running. Please start Docker and run this script again.")
    exit(1)

# Get the network name from the user
aim_network = None
network_names = [network.name for network in client.networks.list()]
print("Available networks:")
print("\n".join(network_names))

# If the network was not found, ask for the network name again
while aim_network is None:
    network_name = input("Please enter the network name: ")
    if network_name not in network_names:
        print("Network not found. Please enter a valid network name.")
    else:
        aim_network = client.networks.get(network_name)
        break

# Create a list to store the container data
containers_data = []

# Print the containers connected to the network
print(f"Containers in {network_name}:")
for container in containers:
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

print("Starting the vulnerability scan...")
input("Press Enter to continue...")

# Scan the containers for vulnerabilities
print("Scanning containers for vulnerabilities with subprocess...")
with open("scan_result.txt", "w") as file:
    file.write("Vulnerability Scan Results with subprocess\n")
    file.write("==========================\n")

for container in containers_data:
    print(f"Scanning {container['Container Name']}...")
    # Scan the container for vulnerabilities
    try:
        result = subprocess.run(['trivy', 'image', container['Service Type']], capture_output=True, text=True)
        # Save the scan result to a text file
        with open("subprocess_scan_result.txt", "a") as file:
            file.write(f"Scan result for {container['Container Name']}:\n")
            file.write(result.stdout)
            file.write("\n")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred while scanning {container['Container Name']}: {str(e)}")
    
    print(f"{container['Container Name']} scanned successfully.")
    print()
