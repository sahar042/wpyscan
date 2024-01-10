from apis.wordfence_api import fetch_vulnerabilities

def check_wordpress_vulnerabilities(wordpress_version):
    if not wordpress_version:
        print("WordPress version not found.")
        return

    print("\n" + "+" + "-" * 50)
    print(f"    Checking vulnerabilities for {wordpress_version}")
    print("+" + "-" * 50 + "\n")

    vulnerabilities = fetch_vulnerabilities()

    if vulnerabilities:
        for vuln_id, details in vulnerabilities.items():
            for software in details['software']:
                if (
                    software['type'] == 'core' and
                    software['name'] == 'WordPress' and
                    version_in_range(wordpress_version, software['affected_versions'])
                ):
                    # print(f"Vulnerability ID: {vuln_id}")
                    print(f"Title:      {details['title']}")
                    # print(f"Description: {details['description']}")
                    print(f"References: {', '.join(details['references'])}")
                    print(f"CVE:        {details.get('cve', 'N/A')}")
                    # print(f"CVSS: {details.get('cvss', 'N/A')}")
                    print(f"Published:  {details.get('published', 'N/A')}")
                    print(f"Updated:    {details.get('updated', 'N/A')}")
                    print("\n" + "=" * 50 + "\n")

def version_in_range(wordpress_version, affected_versions):
    for version, version_details in affected_versions.items():
        from_version = version_details['from_version']
        to_version = version_details['to_version']

        if (
            (from_version == '*' or wordpress_version >= from_version) and
            (to_version == '*' or wordpress_version <= to_version)
        ):
            return True

    return False