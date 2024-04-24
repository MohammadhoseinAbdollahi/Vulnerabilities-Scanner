import requests
import re

def extract_mysql_version(response_text):
    # Regular expression pattern to match MySQL version numbers
    pattern = r'\b\d+\.\d+\.\d+\b'  # Matches version numbers like 5.7.33
    matches = re.findall(pattern, response_text)
    if matches:
        return matches[0]  # Return the first match
    return None
# Function to perform web scraping
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is accessible.")
            # Add your scraping logic here
        else:
            print("Failed to access website. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error accessing website:", e)

def identify_services(url):
    try:
        response = requests.get(url)
        services = {}  # Dictionary to store services and their versions
        if response.status_code == 200:
            headers = response.headers
            server_header = headers.get('Server', '')
            if 'SQL syntax' in response.text:
                services['MySQL'] = 'Unknown version'
            elif '.php' in response.text:
                services['PHP'] = 'Unknown version'
            version = extract_mysql_version(response.text)
            if version:
                services['MySQL'] = version
            if 'Apache' in server_header or 'apache' in server_header or 'httpd' in server_header:
                services['Apache'] = 'Unknown version'
                version = re.search(r'Apache/(\d+\.\d+\.\d+)', server_header)
                if version:
                    services['Apache'] = version.group(1)
            if 'WordPress' in response.text:
                services['WordPress'] = 'Unknown version'
                version = re.search(r'WordPress (\d+\.\d+\.\d+)', response.text)
                if version:
                    services['WordPress'] = version.group(1)
        else:
            print("Failed to access website. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error accessing website:", e)

    return services  # Return the dictionary of services and their versions

def Detecte_services(url):
    # Scrape website
    scrape_website(url)
    # Identify services
    services identify_services(url)



        
        

