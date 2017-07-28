import urllib.request
import os
import sys
import ssl
import urllib.parse
import requests

import requests
import datetime
import json

import re


def load_urls4check(path):
    with open(path) as file:
        # remove http:// or https:// and www. from url
        urls = re.sub('(https?)?:\/\/(www\.)?', '', file.read()).split('\n')
    
    return urls


def parse_urls4http(urls):
    pass


def is_server_respond_with_200(url):
    try:
        request = requests.get(url='http://' + url)
    except requests.exceptions.ConnectionError as error:
        print(error)
    else:
        ok_code = 200
        if request.status_code is ok_code:
            return True


def get_domain_expiration_date(url):
    params = {"apikey":'a7752dbdc9f6086b833baaca5a3f00a9', 'r':'whois', 'domain':'http://' + url}
    request = requests.get('http://api.whoapi.com/', params=params)
    data = request.json()["date_expires"]
    # correct_data = re.sub("[A-Z]", ' ', data)
    correct_data = data
    print(correct_data)
    return correct_data


def get_time_untill_expire(date):
    now = datetime.datetime.now()
    
    # sometimes we see non-standart date format like 2019-03-09-T19:06:45Z, so we need to catch an error
    try:
        expiration_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except ValueError as error:
        print(error)
        # return 'Unknown'
    else:
        time_untill_expire = expiration_date - now
        return time_untill_expire.days


def print_domain_health(url, ok_status, days_left):
    print("%s status: " % url, end='')
    if ok_status:
        print("ok", end=' ')
    else:
        print("NOT RESPONDING", end=' ')
    if days_left < 30:
        print("WARNING, DOMAIN IS EXPIRING SOON: ", end='')
    else:
        pass
    print("%d days left" % days_left)


if __name__ == '__main__':
    path = sys.argv[1]
    # add check for argv len
    urls_to_check = load_urls4check(path)
    print(urls_to_check)
    for url in urls_to_check:
        ok_status = is_server_respond_with_200(url)
        days_till_expire = get_time_untill_expire(get_domain_expiration_date(url))
        print_domain_health(url, ok_status, days_till_expire)