# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:33:52 2018

@author: LIPPA2
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("SanFrancisco.osm", "r")

postcode_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
postcode_types = defaultdict(int)

def audit_tourism_type(postcode_types, postcode):
    m = postcode_type_re.search(postcode)
    print m
    if m:
        postcode = m.group()
        postcode_types[postcode] += 1
                    
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

def is_postcode(elem): 
    return (elem.tag == "tag") and (elem.attrib['k'] == "tourism")


def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_postcode(elem):
            audit_tourism_type(postcode_types, elem.attrib['v'])    
    print_sorted_dict(postcode_types)    

if __name__ == '__main__':
    audit()

"""
apartment: 1
artwork: 54
attraction: 121
camp_site: 10
caravan_site: 1
carousel: 1
chalet: 1
gallery: 11
guest_house: 4
hostel: 15
hotel: 313
information: 114
landmark: 1
memorial: 1
motel: 48
museum: 63
picnic_site: 98
ruins: 16
theatre: 1
theme_park: 1
Tour: 2
viewpoint: 92
zoo: 3
"""
