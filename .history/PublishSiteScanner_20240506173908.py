import requests

def scan_url_with_builtwith(domain):
    api_key = "88f62b83-bc8d-4ac5-9aba-95fa22346760"
    api_url = f"https://api.builtwith.com/free1/api.json?KEY={api_key}&LOOKUP={domain}"

    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Failed to scan URL: {response.text}")
        return None
    data = response.json()
    return data

def extract_technologies(data):
    technologies = []

    groups = data.get("groups", [])
    for group in groups:
        categories = group.get("categories", [])
        for category in categories:
            name = category.get("name", "")
            live = category.get("live", 0)
            dead = category.get("dead", 0)
            latest = category.get("latest", "")
            oldest = category.get("oldest", "")
            technologies.append({
                "name": name,
                "live": live,
                "dead": dead,
                "latest": latest,
                "oldest": oldest
            })

    return technologies

# Example usage
domain = "www.example.com"
data = scan_url_with_builtwith(domain)
if data:
    technologies = extract_technologies(data)
    for tech in technologies:
        print(f"Name: {tech['name']}, Live: {tech['live']}, Dead: {tech['dead']}, Latest: {tech['latest']}, Oldest: {tech['oldest']}")
