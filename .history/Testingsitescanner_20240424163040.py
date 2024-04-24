import requests
from bs4 import BeautifulSoup
import re
from CmsversionFinder import DetectCMSVersion
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except (requests.RequestException, ValueError):
        print(f"Unable to fetch HTML from {url}")
        return None

def extract_frontend_technologies(html,url):
    technologies = set()
    if html is None:
        return technologies

    soup = BeautifulSoup(html, 'html.parser')

    # Extracting JavaScript libraries using script tags
    script_tags = soup.find_all('script', src=True)
    for script_tag in script_tags:
        src = script_tag['src']
        if 'jquery' in src:
            version = re.findall(r'jquery-([0-9\.]+)', src)
            technologies.add(('jQuery', version[0] if version else ''))
        elif 'react' in src:
            version = re.findall(r'react-([0-9\.]+)', src)
            technologies.add(('React', version[0] if version else ''))

    # Extracting CMS using meta tags
    meta_generator_tag = soup.find('meta', attrs={'name': 'generator'})
    if meta_generator_tag:
        content = meta_generator_tag.get('content', '')
        if 'WordPress' in content:
            version = re.findall(r'WordPress ([0-9\.]+)', content)
            technologies.add(('WordPress', version[0] if version else ''))

    # Extracting CMS version from meta tag
    meta_cms_version_tag = soup.find('meta', attrs={'name': 'CMS-version'})
    if meta_cms_version_tag:
        version = meta_cms_version_tag.get('content', '')
        technologies.add(('CMS', version))
    # Extracting frontend frameworks using link tags
    link_tags = soup.find_all('link', rel=True)
    for link_tag in link_tags:
        rel = link_tag['rel']
        if 'stylesheet' in rel:
            href = link_tag['href']
            if 'bootstrap' in href:
                version = re.findall(r'bootstrap-([0-9\.]+)', href)
                technologies.add(('Bootstrap', version[0] if version else ''))
            elif 'foundation' in href:
                version = re.findall(r'foundation-([0-9\.]+)', href)
                technologies.add(('Foundation', version[0] if version else ''))
    # Extracting 
    

    return technologies

# Example usage
url = "https://www.vatanzarin.com/"
html = fetch_html(url)
if html:
    frontend_technologies = extract_frontend_technologies(html,url)
    cms_versions = DetectCMSVersion(url)
    print("Detected frontend technologies:")
    for tech, version in frontend_technologies:
        print(f"{tech}: {version}")