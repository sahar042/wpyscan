from apis.wordfence_api import fetch_vulnerabilities

def check_plugin_vulnerabilities(name, version=None, software_type=None):
    if not name:
        print("Name information not provided.")
        return

    vulnerabilities = fetch_vulnerabilities()
    found_vulnerabilities = False

    if vulnerabilities:
        for vuln_id, details in vulnerabilities.items():
            for software in details['software']:
                if (
                    name == software['slug'] and
                    (version is None or version_in_range(version, software['affected_versions']))
                ):
                    # print(f"Vulnerability ID: {vuln_id}")
                    print(f"    Title:      {details['title']}")
                    # print(f"Description: {details['description']}")
                    print(f"    References: {', '.join(details['references'])}")
                    print(f"    CVE:        {details.get('cve', 'N/A')}")
                    # print(f"CVSS: {details.get('cvss', 'N/A')}")
                    print(f"    Published:  {details.get('published', 'N/A')}")
                    print(f"    Updated:    {details.get('updated', 'N/A')}")
                    print("")
                    found_vulnerabilities = True
                    break

        if not found_vulnerabilities:
            print(f"   [-] {name}{' ' + version if version else ''} has no known vulnerabilities.")

def version_in_range(input_version, affected_versions):
    for version, version_details in affected_versions.items():
        from_version = version_details.get('from_version')
        to_version = version_details.get('to_version')

        if (
            (from_version is None or (input_version and input_version >= from_version)) and
            (to_version == '*' or (input_version and input_version <= to_version))
        ):
            return True

    return False