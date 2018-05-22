from player import *
from exceptions import *
import country as ctry
from country import USA, USSR, NEU

def check_country_name(func):  
    def wrapper(*args, **kwargs):
        if args[0] not in ctry.country:
            raise CountryNotFoundError(args[0])
        return func(*args, **kwargs)
    return wrapper

def id(item):
    if item == USA:
        return 2
    elif item == USSR:
        return 3
    elif item == 'sta':
        return 1
    elif item == 'bf':
        return 0
    else:
        raise InvalidArgumentError(item)

@check_country_name
def force_of(country_name):
    if ctry.country[country_name][id(USA)] - ctry.country[country_name][id(USSR)] >= ctry.country[country_name][id('sta')]:
        return USA
    elif ctry.country[country_name][id(USSR)] - ctry.country[country_name][id(USA)] >= ctry.country[country_name][id('sta')]:
        return USSR
    else:
        return NEU

@check_country_name
def update_inf(country_name, force, diff):
    ctry.country[country_name][id(force)] = max(0, ctry.country[country_name][id(force)] + diff)

@check_country_name
def set_inf(country_name, force, value):
    ctry.country[country_name][id(force)] = value

@check_country_name
def get_inf(country_name, force):
    return ctry.country[country_name][id(force)]

@check_country_name
def is_battle(country_name):
    return ctry.country[country_name][id('bf')]

@check_country_name
def region_of(country_name):
    return visit(ctry.region, None, trace, country_name)

def trace(region, ancestor, country_name):
    for v in region:
        if v == country_name:
            return ancestor

# arglis -> 搜索的路径
# method -> 对list调用的方法
# *args -> method的除arglis之外的参数
def visit(region, arglis, method, *args):
    if arglis is None:
        arglis = ()
    if type(region) == dict:
        for k in region:
            res = visit(region[k], arglis + (k,), method, *args)
            if res is not None:
                return res
        return None
    else:
        return method(region, arglis, *args)