import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import re
from PredictTheDatabaseVersion 

def extract_cms_version(url):
    cms_versions = []

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Approach 1: Check meta tags for generator tag
            generator_tag = soup.find('meta', {'name': 'generator'})
            if generator_tag:
                cms_versions.append(generator_tag.get('content'))

            # Approach 2: Parse HTML comments for CMS version information
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            for comment in comments:
                if 'WordPress' in comment:
                    cms_versions.append(comment.split('WordPress')[1].strip())

            # Approach 3: Check URL path for common CMS patterns
            if 'wordpress' in url.lower():
                cms_versions.append('WordPress')  # Assuming WordPress if 'wordpress' is in URL
            
            # Approach 4: Check for specific class or id in the HTML structure
            specific_class_or_id = soup.find(class_='specific-class')  # Replace 'specific-class' with your desired class
            if specific_class_or_id:
                # Extract version information from class or id
                version_text = specific_class_or_id.get_text()
                # Perform version extraction based on specific pattern
                version = re.search(r'(\d+\.\d+(\.\d+)?)', version_text)
                if version:
                    cms_versions.append(version.group(1))

            # Approach 5: Check for specific text patterns in the HTML structure
            specific_text_pattern = soup.find(string=re.compile(r'Wordpress Version: \d+\.\d+(\.\d+)?'))
            if specific_text_pattern:
                version_text = specific_text_pattern.strip()
                version = re.search(r'(\d+\.\d+(\.\d+)?)', version_text)
                if version:
                    cms_versions.append(version.group(1))

        else:
            print(f"Failed to retrieve URL: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
    return cms_versions
url = "https://mobileland.online"



def DetectCMSVersion(url):
    versions = extract_cms_version(url)
    if versions:
        s = versions[0]
        s = s.replace('WordPress: ', '')  # Remove 'WordPress: ' from the string
        version = s.split(".")[0:2]  # Split the string on "." and take the first two parts
        version = ".".join(version)  # Join the parts back together with "."
        s = f"CMS {version}"  # Format the string with "CMS" at the start
        s = s.replace('WordPress ', '')  # Remove 'WordPress ' from the string
           
    else:
        print("Could not detect CMS versions.")
DetectCMSVersion(url)