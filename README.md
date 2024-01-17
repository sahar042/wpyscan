![WPyScan](wpyscan_banner.png)
---
<div align="center">

![version](https://img.shields.io/badge/version-1.0.0-blue)
![build](https://img.shields.io/badge/build-passing-green)
![license](https://img.shields.io/badge/license-GPLv3-lightgrey)

![python](https://img.shields.io/badge/Python-3.12-FFDA4A.svg?style=flat&logo=python&logoColor=white&labelColor=blue)

</div>

A tool developed in Python for enumerating and scanning **WordPress** websites. It is an easy-to-use tool that can be run from the command line. **WPyScan** can enumerate and find any vulnerability associated with **version**, **theme** and **plugins** installed.

## Features
- **FREE UNLIMITED** API queries
- **WordFence** WordPress Vulnerability Database
- **Brute Force** enumeration available for almost any check
- **WAF Bypass** with random user agents by default
- **Measures for CAPTCHA avoidance**

> **WARNING**
>
> **WPyScan has been launched but not thoroughly tested.** Please, open any issue you encounter and help improve the tool. The code is dirty and full of bad practices. I am not a developer but a hacker. If you want to contribute, you are welcome.
{: .prompt-warning }

![Screenshot](https://github.com/amtzespinosa/wpyscan/raw/main/img/screenshot_1.png)

## What can WPyScan check for?
- The version of WordPress installed and any associated vulnerabilities
- What plugins are installed and any associated vulnerabilities
- What themes are installed and any associated vulnerabilities
- Username enumeration
- Users with weak passwords via password brute forcing
- Backed up and publicly accessible wp-config.php files
- Database dumps that may be publicly accessible
- If error logs are exposed by plugins
- Media file enumeration
- If the WordPress readme file is present
- If WP-Cron is enabled
- If user registration is enabled
- Full Path Disclose
- Upload directory listing
- And much more... **AND FOR FREE WITH NO LIMITS**

## Usage
By now, only simple use is available. Clone the repo, get inside the folder and:

```
sudo python3 main.py -u [URL]
```

URL format: https://example.com/

> **SCANS WILL TAKE LONG**
>
> Due to the many scans performed and the avoidance of security measures implemented by the websites, scans are slow. Be patient.
{: .prompt-warning }

## Modules
Documentation is on its way! 

# TODO
- [ ] Test, test, test... and test!
- [ ] Clean the code
- [ ] Compile it in a tool, not just single scripts **(I am having troubles with this so any help will be welcome!)**
- [ ] Polish all the modules and their execution
- [ ] Make it more precise and reliable
- [ ] And a few more things!
