# rss.py

import requests
import re

def extract_wordpress_version_rss(url):
    method = "RSS (Passive Detection)"
    feed_url = url.rstrip('/') + "/feed"
    try:
        response = requests.get(feed_url)
        if 200 <= response.status_code < 300:
            match = re.search(r'<generator>https://wordpress.org/\?v=(\d+\.\d+(\.\d+)?)</generator>', response.text)
            if match:
                version = match.group(1)
                return version, method
    except requests.RequestException:
        pass
    return None
