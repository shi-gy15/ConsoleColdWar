import country
from exceptions import *

def check_country(region):
    if type(region) == dict:
        for k in region:
            check_country(region[k])
    else:
        for v in region:
            if v not in country.country:
                print('[In check_country] ' + 'Country not found: ' + v)

def auto_check():
    print('[In auto_check]')
    check_country(country.region)
    