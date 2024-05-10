from vulners import Vulners
import subprocess
Wordpress_version=""
api_key_Mysql_apache = "M2RMANQBW9I5AAIJ1DBZZLNW63YTTQ2I0PVR488D9U0YW3P88HYBV6RV5VZL0IZ2"
api_token_wpscan = 'bzGYb0wY5MIwW05sbtXbZDWqVxUtn4xV12gGgQmMUGg'

def search_vulnerabilities(service_name, service_version,api_key):
    vulners_api = Vulners(api_key)
    # Search for vulnerabilities related to the service name and version
    vulnerabilities = vulners_api.softwareVulnerabilities(service_name, service_version)
    return vulnerabilities

def display_vulnerabilities_MySQL_Apache(vulnerabilities):
    if vulnerabilities:
        output_file = "/Users/mohammadhosein/Documents/FSTT/outputs/output.txt"
        with open(output_file, "a") as file:
            if vulnerabilities:
                file.write("Vulnerabilities found:\n")
            for cve_id, vulnerability_list in vulnerabilities.items():
                for vulnerability in vulnerability_list:
                    file.write("- CVE ID: {}\n".format(cve_id))
                    file.write("  Description: {}\n".format(vulnerability.get('description')))
                    file.write("  CVSS Score: {}\n".format(vulnerability.get('cvss', {}).get('score')))
                    file.write("\n")  # Add a blank line for readability
            else:
                file.write("No vulnerabilities found.")
            file.write("---------------------------------------------------------------")
        print("Output saved to:", output_file)
    
def wpscan_version(site_url, api_token):
    try:
        # Construct the WPScan command without specifying the WordPress version
        command = ['wpscan', '--url', site_url, '--enumerate', 'vp', '--no-update', '--api-token', api_token]
        print("Running WPScan command:", " ".join(command))
        # Execute the WPScan command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        # Print the WPScan output
        output_file = "/Users/mohammadhosein/Documents/FSTT/outputs/outputWPscan.txt"
        with open(output_file, "a") as file:
            file.write(result.stdout)
            file.write("---------------------------------------------------------------")
            print("Output saved to:", output_file)

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during WPScan execution
        print(f"An error occurred: {e}")
        vulnerabilities = search_vulnerabilities("WordPress", Wordpress_version,api_key_Mysql_apache)
        display_vulnerabilities_MySQL_Apache(vulnerabilities)
        

def identify_vulnerabilities(services, site_url):
    # Identify vulnerabilities in the specified environment
    print("Identifying vulnerabilities...")
    # Check for vulnerabilities in the services
    for service_name, service_version in services.items():
        if service_name == "WordPress":
            Wordpress_version = service_version
            wpscan_version(site_url,api_token_wpscan)
        else:
            vulnerabilities = search_vulnerabilities(service_name, service_version,api_key_Mysql_apache)
            display_vulnerabilities_MySQL_Apache(vulnerabilities)
        
        

