import sys
import requests
import datetime
import re


def load_urls4check(path):
    with open(path) as file:
        # remove http:// or https://
        urls = re.sub('(https?)?:\/\/', '', file.read()).split('\n')
    return urls


def is_server_respond_with_200(url):
    try:
        request = requests.get(url='http://' + url)
    except requests.exceptions.ConnectionError:
        return False
    else:
        if request.ok:
            return True

def load_api_key():
    try:
        with open('key.txt') as file:
            key = file.read()
    except FileNotFoundError:
        print("Failed to load key.txt. Whois service is not availabe.")
    else:
        if len(key) > 1:
            return key
        else:
            return None
    


def get_domain_time_untill_expire(url, api_key):
    if api_key:
        params = {"apikey":api_key, 'r':'whois', 'domain':'http://' + url}
        request = requests.get('http://api.whoapi.com/', params=params)
        answer = request.json()
        if answer["registered"]:
            expiration_date = datetime.datetime.strptime(answer["date_expires"], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            time_untill_expire = expiration_date - now
            return time_untill_expire.days
    else:
        return -1

def print_site_health_info(url, ok_status, expiration_info):
    if ok_status:
        print("%s status code: ok" % url)
    else:
        print("%s is down!" % url)
    
    if expiration_info:
        if expiration_info > 30:
            print('Domain health ok. %d days until expire.' % expiration_info)
        elif expiration_info is -1:
            pass
        else:
            print("Warning! Domain will expire in %s days!" % expiration_info)
    else:
        print("Domain is not registered.")


def main():
    if len(sys.argv) < 2:
        print("Usage: check_sites_health.py [path]. Also dont forget key.txt")
        exit()
    path = sys.argv[1]
    urls_to_check = load_urls4check(path)
    api_key = load_api_key()
    for url in urls_to_check:
        print('...')
        ok_status = is_server_respond_with_200(url)
        expiration_info = get_domain_time_untill_expire(url, api_key)
        print_site_health_info(url, ok_status, expiration_info)


if __name__ == '__main__':
    main()
    #print(load_api_key())
    #print(len(sys.argv))
