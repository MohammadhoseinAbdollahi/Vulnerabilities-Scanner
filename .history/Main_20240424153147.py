# This is the main file that will be executed to run the scanning program.
import os
from Dockerscanvul import DockerScanner
def main():
    print("Welcome to the scanning program!")
    print("Please select the scanning environment:")
    print("1. Docker")
    print("2. Localhosts")
    print("3. Websites")
    print("4. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # chek if docker is installed
        if os.system("docker --version") != 0:
            print("Docker is not installed. Please install Docker and try again.")
            main()
        # check if trivy is installed
        if os.system("trivy --version") != 0:
            print("Trivy is not installed. Please install Trivy and try again.")
            main()
        
        network_name = input("Enter the network name: ")
        scanner = DockerScanner()
        scanner.scan_containers_in_network(network_name)
        print("Scanning completed!")
        print("Please check the generated PDF files for the scan results.")
        print("But, If you want to see what is inside container prees 1 else press 2")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            print("wait for this part")
        else:
            print("ok")
            main()
            
    elif choice == "2":
        url = input("Enter the URL: ")
        # TODO: Perform scanning on localhost using the provided URL

    elif choice == "3":
        url = input("Enter the URL: ")
        # TODO: Perform scanning on the specified website using the provided URL
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        return

    else:
        print("Invalid choice. Please try again.")
        return

if __name__ == "__main__":
    main()