# comments.py

import requests
import re
from user_agents import get_random_user_agent

def extract_wordpress_version_meta(url):
    method = "Meta Generator (Passive Detection)"
    try:
        # response = requests.get(url)
        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(url, headers=headers, allow_redirects=True)

        if 200 <= response.status_code < 300:
            match = re.search(r'<meta name="generator" content="WordPress ([0-9.]+)"', response.text)
            if match:
                version = match.group(1)
                return version, method
    except requests.RequestException:
        pass
    return None