import requests
import json



def query_cve(self, product_name, version):
    base_url = "https://cve.circl.lu/api/search"
    params = {
        "product": product_name,
        "version": version
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        
        
def query_nvd(product_name, version):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    params = {
        "keyword": f"{product_name} {version}"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
vulnerabilities = query_cve("apache", "2.4.46")
print(vulnerabilities)
vulnerabilities 