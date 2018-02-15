# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:38:42 2018

@author: LIPPA2
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("map_sfo.osm", "r")

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
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:city")


def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_postcode(elem):
            audit_tourism_type(postcode_types, elem.attrib['v'])    
    print_sorted_dict(postcode_types)    

if __name__ == '__main__':
    audit()
    
"""
Alamda: 1
alameda: 1
Alameda: 132
Albany: 238
Beach: 3
Berkeley: 5772
berkeley: 2
Brisbane: 7
CA: 6
Ca: 1
Canyon: 2
Cerrito: 40
City: 100
Colma: 31
Emeryville: 55
Emeyville: 7
Francisco: 19374
Kensington: 1
Leandro: 38
oakland: 21
OAKLAND: 2
Oakland: 1397
Okaland: 2
Orinda: 6
Pacifica: 39
Piedmont: 3812
Richmond: 1
Sausalito: 65
Strawberry: 1
Tiburon: 7
Valley: 26
"""