import requests
import json


class SecurityAssignment:
    def query_cve(product_name, version):
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