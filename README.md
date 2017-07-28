# Sites Monitoring Utility

This script will help you monitor sites health
It will check web site status and domain expiration time left.
# Installation:
Python 3 required.

To install additional packages you should run this command from folder with where you downloaded script.
```
pip3 instal -r requirements.txt
```

# Usage:

You need to create a text file with urls you want to check. 

sites.txt:
```
facebook.com
ya.ru
megaupload.com
specialized.com
```

Run this script using python 3 with a path as an argument.
```
check_sites_health.py [path]
```

Example:
```
check_sites_health.py sites.txt
...
facebook.com status: ok
Domain health ok. 2801 days until expire.
...
ya.ru status: ok
Warning! Domain will expire in 3 days
...
megaupload.com is down!
Domain health ok. 236 days until expire.
...
specialized.com status: ok
Domain health ok. 3384 days until expire.

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
