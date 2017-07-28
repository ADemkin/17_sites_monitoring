import sys
import requests
import datetime
import re


def load_urls4check(path):
    with open(path) as file:
        # remove http:// or https:// and www. from url
        urls = re.sub('(https?)?:\/\/(www\.)?', '', file.read()).split('\n')
    return urls


def is_server_respond_with_200(url):
    try:
        request = requests.get(url='http://' + url)
    except requests.exceptions.ConnectionError:
        return False
    else:
        ok = 200
        if request.status_code is ok:
            return True


def get_domain_time_untill_expire(url):
    # using api for whoapi.com to check whois on a certain domain
    params = {"apikey":'a7752dbdc9f6086b833baaca5a3f00a9', 'r':'whois', 'domain':'http://' + url}
    request = requests.get('http://api.whoapi.com/', params=params)
    answer = request.json()
    if answer["registered"]:
        expiration_date = datetime.datetime.strptime(answer["date_expires"], '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        time_untill_expire = expiration_date - now
        return time_untill_expire.days


if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        path = sys.argv[1]
        urls_to_check = load_urls4check(path)
        
        for url in urls_to_check:
            print('...')
            
            if is_server_respond_with_200(url):
                print("%s status: ok" % url)
            else:
                print("%s is down!" % url)
            
            expiration_info = get_domain_time_untill_expire(url)
            if expiration_info:
                if expiration_info > 30:
                    print('Domain health ok. %d days until expire.' % expiration_info)
                else:
                    print("Warning! Domain will expire in %s days" % expiration_info)
            else:
                print("Domain is not registered.")
    else:
        print("Usage: check_sites_health.py [path]")
