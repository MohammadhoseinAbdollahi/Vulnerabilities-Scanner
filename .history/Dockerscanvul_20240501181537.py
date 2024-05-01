import subprocess
import json
import os

def get_image_name_from_container(container_name):
    command = ["docker", "inspect", container_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Failed to inspect container: {stderr.decode()}")
        return None

    data = json.loads(stdout.decode())
    return data[0]['Config']['Image']

def get_containers_in_network(network_name):
    command = ["docker", "network", "inspect", network_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Failed to inspect network: {stderr.decode()}")
        return []

    data = json.loads(stdout.decode())
    return [container['Name'] for container in data[0]['Containers'].values()]

def scan_container_with_trivy(image_name):
    command = ["docker", "images", "-q", image_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0 or not stdout:
        print(f"Docker image {image_name} not found")
        return

    output_folder = os.path.join(os.getcwd(), "outputs")
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, f"{image_name}_vulnerabilities.txt")
    command = ["trivy", "image", "--output", output_file, image_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Failed to scan container: {stderr.decode()}")

def DockerScanner(network_name):
    containers = get_containers_in_network(network_name)
    print(f"Containers in network {network_name}: {containers}")
    
    for container in containers:
        image_name=get_image_name_from_container(container)
        scan_container_with_trivy(image_name)

    