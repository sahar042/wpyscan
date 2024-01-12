# /wp-json/wp/v2/users
# {"id":296,"name":"Bohdan Shila","url":"","description":"","link":"https:\/\/sinoficina.com\/author\/bohdan\/","slug":"bohdan","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/54a35f40eec767188d8e05c6da87ac82?s=24&d=mm&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/54a35f40eec767188d8e05c6da87ac82?s=48&d=mm&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/54a35f40eec767188d8e05c6da87ac82?s=96&d=mm&r=g"},"meta":[],"acf":[],"yoast_head":null,"yoast_head_json":null,"_links":{"self":[{"href":"https:\/\/sinoficina.com\/wp-json\/wp\/v2\/users\/296"}],"collection":[{"href":"https:\/\/sinoficina.com\/wp-json\/wp\/v2\/users"}]}}

import requests, json, time
from avoidance.user_agents import get_random_user_agent
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WPJsonApi:
    def __init__(self, api_url):
        self.api_url = api_url

    def aggressive(self):
        try:
            headers = {'User-Agent': get_random_user_agent()}
            response = requests.get(self.api_url, headers=headers)

            if 200 <= response.status_code < 300:
                if self.detect_captcha(response.text):
                    print(" |- Captcha or redirect detected. Handle accordingly.")
                else:
                    json_data = response.json()
                    if 'slug' in json_data and json_data['slug']:
                        self.print_user_details(json_data)
                    else:
                        print("[-] No user details found in the WordPress JSON API response.")
            else:
                if "captcha" in response.text:
                    print(f" |- Error: {response.status_code} - Possible CAPTCHA block.")
                else:
                    print(f" |- Error: {response.status_code}")

        except (json.JSONDecodeError, requests.RequestException) as e:
            pass

    def detect_captcha(self, response_text):
        return "Captcha" in response_text or "redirect" in response_text

    def print_user_details(self, json_data):
        usernames = []
        if 'slug' in json_data and json_data['slug']:
            username = json_data['slug']
        if 'name' in json_data and json_data['name']:
            name = json_data['name']
        user_dict = {username: name}
        for result in json_data:
            if user_dict not in usernames:
                usernames.append(user_dict)
                print(f"[+] Username: {username}")
                print(f" |- Author Name: {json_data['name']}")
            else:
                usernames.append(user_dict)

class WPJsonApiProxy:
    def __init__(self, api_url, proxy_api=None):
        self.api_url = api_url
        self.proxy_api = proxy_api
        self.proxy_list = self.fetch_proxy_api()

    def fetch_proxy_api(self):
        try:
            response = requests.get(self.proxy_api)
            if response.status_code == 200:
                return [self.parse_proxy_line(line) for line in response.text.strip().split('\n') if line.strip()]
            else:
                print(f"Error fetching proxy information from API. Status code: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Error fetching proxy information from API: {e}")
            return []

    def parse_proxy_line(self, line):
        host, port = line.split(':')
        return {"host": host, "port": int(port)}

    def get_requests_session(self, proxy):
        session = requests.Session()

        if proxy:
            session.proxies = {
                'http': f"socks5://{proxy['host']}:{proxy['port']}",
                'https': f"socks5://{proxy['host']}:{proxy['port']}",
            }
            session.verify = False  # You may want to remove this line if the proxy supports HTTPS

        return session

    def aggressive(self):
        max_retries = 3
        retry_delay = 5  # seconds
        max_polling_attempts = 10
        polling_interval = 5  # seconds

        for proxy_info in self.proxy_list:
            print(f" |- Trying with proxy: {proxy_info['host']}:{proxy_info['port']}")
            for attempt in range(1, max_retries + 1):
                try:
                    session = self.get_requests_session(proxy_info)
                    headers = {'User-Agent': get_random_user_agent()}
                    response = session.get(self.api_url, headers=headers)

                    if response.status_code == 202:
                        print(f" |- Waiting for processing to complete. Attempt {attempt}/{max_retries}...")
                        for _ in range(max_polling_attempts):
                            time.sleep(polling_interval)
                            response = session.get(self.api_url, headers=headers)
                            if response.status_code != 202:
                                break

                    if 200 <= response.status_code < 300:
                        if response.text.strip():
                            json_data = response.json()
                            if isinstance(json_data, list):
                                print("[+] Usernames found:")
                                for user_data in json_data:
                                    self.print_user_details(user_data)
                            else:
                                self.print_user_details(json_data)
                            return  # Exit the loop if successful
                        else:
                            print("[-] Empty response from the WordPress JSON API.")
                            break
                    else:
                        if "captcha" in response.text:
                            print(f" |- Error: {response.status_code} - Possible CAPTCHA block.")
                        else:
                            print(f" |- Error: {response.status_code}")
                        break

                except (json.JSONDecodeError, requests.RequestException) as e:
                    print(f" |- Error: {e}")
                    break

        print("[-] Failed to obtain a successful response with any proxy.")

    def print_user_details(self, json_data):
        try:
            username = json_data.get('slug', '')
            name = json_data.get('name', '')

            if username:
                print(f" |- Author Name: {name}")
                print(f" |- Username: {username}")
                print(" |")
            else:
                print("[-] No username found in the WordPress JSON API response.")
        except Exception as e:
            print(f" |- Error parsing user details: {e}")