import sys
import requests
import datetime
import re


def keep_only_urls_with_valid_protocol(urls):
    # check if url contain exactly http:// or https://
    protocols_regexp = re.compile('https?:\/\/')
    valid_urls = []
    for url in urls:
        match = protocols_regexp.match(url)
        if match:
            valid_urls.append(url)
        else:
            print("{} is not a valid url. Protocol is missing.".format(url))
    return valid_urls


def load_urls4check(path):
    try:
        with open(path) as file:
            all_urls = file.read().split('\n')
    except FileNotFoundError as error:
        print('{}: {}'.format(error.strerror, path))
        exit()
    else:
        return keep_only_urls_with_valid_protocol(all_urls)


def is_server_respond_with_200(url):
    try:
        request = requests.get(url=url)
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
        print("Failed to load key.txt. Whois service is not available.")
    else:
        if key:
            return key
        else:
            return None


def get_domain_time_untill_expire(url, api_key):
    if api_key:
        params = {"apikey":api_key, 'r':'whois', 'domain':url}
        request = requests.get('http://api.whoapi.com/', params=params)
        answer = request.json()
        if answer["registered"]:
            expiration_date = datetime.datetime.strptime(answer["date_expires"], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            time_untill_expire = expiration_date - now
            return time_untill_expire.days


def print_site_health_info(url, ok_status, expiration_info):
    if ok_status:
        print("%s status: ok" % url)
    else:
        print("%s is down" % url)
    
    if expiration_info:
        if expiration_info > 30:
            print('Domain health ok. %d days until expire.' % expiration_info)
        else:
            print("Warning! Domain will expire in %s days!" % expiration_info)
    else:
        print("No data on this domain.")


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
