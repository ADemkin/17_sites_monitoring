# Sites Monitoring Utility

This script will help you monitor sites health
It will check web site status and domain expiration time left.

Anton Demkin, 2017

antondemkin@yandex.ru
# Installation:
Python 3 required.

To install additional packages you should run this command from folder with where you downloaded script.
```
pip3 instal -r requirements.txt
```

# Usage:

You need to create a text file with urls you want to check. To use [whois](whoapi.com) service you need to [register](https://whoapi.com/user/signup), 
receive your personal api key and put it into key.txt into the same folder with your check_sites_health.py script.

Text file with urls __must__ contain a valid urls with protocol. If you dont specify protocol, the url wont be checked.

__sites.txt:__ (you may use your own file name)
```
https://www.facebook.com
https://www.ya.ru
http://megaupload.com
http://specialized.com
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
