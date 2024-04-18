import docker
import json

# Connect to the Docker Network
client = docker.from_env()

input

# Find the monitoring_network
aim_network = client.networks.get('monitoring_network')

# Create a list to store the container data
containers_data = []

# If the network was found, print the names of all containers in it
if aim_network is not None:
    # Print the containers connected to the network
    print("Containers in monitoring_network:")
    for container in aim_network.containers:
        container_info = container.attrs
        container_name = container_info['Name']
        container_ipv4 = container_info['NetworkSettings']['Networks']['monitoring_network']['IPAddress']
        url = f"http://{container_ipv4}"  # Assuming the URL is the container's IP address
        port = list(container_info['NetworkSettings']['Ports'].keys())[0]  # Assuming the port is the first exposed port
        service_type = container_info['Config']['Image']  # Assuming the service type is the container's image

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

    # Write the data to a JSON file
    with open('input.json', 'w') as f:
        json.dump(containers_data, f, indent=4)

else:
    print("Network 'monitoring_network' not found")