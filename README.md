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

You need to create a text file with urls you want to check. To use [whois](whoapi.com) service you need to register, 
receive your personal api key and put it into key.txt into the same folder with your check_sites_health.py script.

__sites.txt:__
```
facebook.com
ya.ru
megaupload.com
specialized.com
```

__key.txt:__
```
fe7fa75b11aaf41fa205ba292787fd74
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
