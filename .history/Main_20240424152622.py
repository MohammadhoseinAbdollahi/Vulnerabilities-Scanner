# This is the main file that will be executed to run the scanning program.
import os
from Dockerscanvul import DockerScanner
def main():
    print("Welcome to the scanning program!")
    print("Please select the scanning environment:")
    print("1. Docker")
    print("2. Localhosts")
    print("3. Websites")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        network_name = input("Enter the network name: ")
        scanner = DockerScanner()
        scanner.scan_containers_in_network(network_name)
        print("Scanning completed!")
        print("Please check the generated PDF files for the scan results.")
        print("But, If you want to see what is inside container prees 1 else press 2")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            pri

    elif choice == "2":
        url = input("Enter the URL: ")
        # TODO: Perform scanning on localhost using the provided URL

    elif choice == "3":
        url = input("Enter the URL: ")
        # TODO: Perform scanning on the specified website using the provided URL

    else:
        print("Invalid choice. Please try again.")
        return

if __name__ == "__main__":
    main()