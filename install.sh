#!/bin/bash
pip install requests urllib re bs4

cp -r wpyscan/ /usr/lib/wpyscan/
cp wpyscan /usr/bin/
chmod +x /usr/bin/wpyscan
cp wpyscan-uninstall /usr/bin/
chmod +x /usr/bin/wpyscan-uninstall

