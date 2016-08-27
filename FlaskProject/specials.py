# James Anderson 20160821
# Created functions to assist with the "specials" page

import json
from datetime import datetime

def get_specials(filename):
    f = open(filename)
    specials = json.load(f)
    f.close()
    return specials


def get_special():
    specials = get_specials('specials.json')
    today = datetime.now()
    DAYS_OF_WEEK = ('monday', 'tuesday', 'wednesday',
                     'thursday', 'friday', 'saturday', 'sunday')
    weekday = DAYS_OF_WEEK[today.weekday()]
    return specials[weekday]