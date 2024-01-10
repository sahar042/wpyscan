# readme.py

import re
import requests

def extract_wordpress_version_readme(url):
    method = "Readme (Passive Detection)"
    try:
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            match = re.search(r'Stable tag: (\d+\.\d+(\.\d+)?)', response.text)
            if match:
                version = match.group(1)
                return version, method
    except requests.RequestException:
        pass
    return None
