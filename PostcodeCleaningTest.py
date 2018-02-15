# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:02:35 2018

@author: LIPPA2
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:28:50 2017

@author: LIPPA2
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("map_sfo.osm", "r")

postcode_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
postcode_types = defaultdict(int)

def audit_postcode_type(postcode_types, postcode):
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
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:postcode")


def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_postcode(elem):
            audit_postcode_type(postcode_types, elem.attrib['v'])    
    print_sorted_dict(postcode_types)    

if __name__ == '__main__':
    audit()

"""
14123: 1
41907: 1
90214: 6
93710: 1
94005: 4
94013: 1
94014: 50
94015: 71
94017: 1
94044: 40
94080: 101
94087: 1
94102: 220
94103: 830
94103-3124: 1
94104: 76
94105: 142
94107: 153
94108: 141
94109: 481
94110: 259
94111: 75
94112: 50
94113: 80
94114: 371
94115: 87
94115-4620: 1
94116: 2409
94117: 1510
94117-9991: 1
94118: 1138
94118-1316: 1
94118-4504: 1
94121: 394
94121-1545: 1
94121-3131: 1
94122: 5129
94122-1515: 3
94123: 158
94124: 56
94127: 851
94129: 11
94130: 3
94131: 173
94132: 67
94133: 1125
94134: 25
94143: 7
94158: 29
94164: 1
94166: 4
94188: 1
94501: 128
94502: 5
94516: 2
94530: 40
94563: 6
94577: 38
94579: 3
94601: 73
94602: 72
94603: 6
94605: 26
94606: 142
94606-3636: 2
94607: 119
94608: 107
94609: 43
94610: 1359
94611: 2993
94612: 118
94612-2202: 1
94613: 6
94618: 79
94619: 37
94621: 17
94702: 86
94703: 67
94704: 170
94705: 37
94706: 178
94707: 19
94708: 5
94709: 41
94710: 57
94720: 5
94720-1076: 1
94804: 11
94901: 2
94920: 8
94941: 24
94965: 64
94970: 1
95115: 1
95430: 2
95476: 2
ca: 1
CA: 3
"""