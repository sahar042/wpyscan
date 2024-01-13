#!/bin/bash
pip install requests urllib3 beautifulsoup4

cd ..
cp -r wpyscan/ /usr/lib/wpyscan/
cd wpyscan
cp wpyscan /usr/local/bin/
chmod +x /usr/local/bin/wpyscan
cp wpyscan-uninstall /usr/local/bin/
chmod +x /usr/local/bin/wpyscan-uninstall

