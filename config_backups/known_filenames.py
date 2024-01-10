import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

class ConfigBackup:
    def __init__(self, url):
        self.url = url

class KnownFilenames:
    def __init__(self, target):
        self.target = target

    def aggressive(self, opts=None):
        found = []

        for filename in self.get_potential_filenames():
            url = urljoin(self.target, filename)
            res = requests.get(url)
            
            if res.status_code == 200 and re.search(r'define', res.text, re.I) and not re.search(r'<\s?html', res.text, re.I):
                found.append(ConfigBackup(url))

        return found

    def get_potential_filenames(self):
        # Replace with your own array of potential filenames
        return ['wp-config.php', 'config.php', 'settings.php']
