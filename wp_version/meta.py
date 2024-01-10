# meta.py

import re
import requests

def extract_wordpress_version_meta(url):
    method = "Meta Generator (Passive Detection)"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            match = re.search(r'content=["\']WordPress (\d+\.\d+(\.\d+)?)', response.text)
            if match:
                version = match.group(1)
                return version, method

    except requests.RequestException:
        pass
    return None, None
