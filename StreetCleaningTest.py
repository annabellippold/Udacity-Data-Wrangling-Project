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

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    print m
    if m:
        street_type = m.group()
        street_types[street_type] += 1
                    
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

def is_street_name(elem): 
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")


def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])    
    print_sorted_dict(street_types)    

if __name__ == '__main__':
    audit()

"""
#105: 1
#151: 1
#155: 1
#203: 1
#3500: 1
#404: 1
#411: 1
1: 1
122°29'07.1"W: 1
15: 1
15th: 1
2: 1
3658: 1
39: 4
4.5: 1
730: 2
A: 3
Alameda: 40
Alley: 22
Alto: 3
AVE: 1
Ave: 17
Ave.: 3
Avenue: 12470
B: 2
Bldg: 1
Blvd: 7
Blvd.: 1
Boulevard: 949
Bridgeway: 22
broadway: 2
Broadway: 149
Building: 3
California: 1
Center: 43
Circle: 36
Court: 236
Crescent: 2
Ctr: 2
Cut: 1
D: 5
Drive: 999
E: 1
East: 1
Embarcadero: 19
F: 1
Ferlinghetti: 1
Francisco: 1
Freeway: 1
G: 1
Gardens: 57
Gough: 1
H: 12
Hall: 1
Highway: 46
Hill: 3
Hwy: 1
Hyde: 1
King: 1
Landing: 3
Lane: 95
Loma: 1
M: 1
Mall: 1
Mar: 1
Marina: 4
Mason: 27
Montgomery: 2
Ness: 1
North: 5
Overlook: 1
Palms: 3
Park: 7
Parkway: 10
Path: 18
Pier: 1
Pl: 1
Place: 189
Plaza: 66
Pollard: 1
Post: 1
Powell: 1
Rd: 1
Real: 13
Road: 726
Rock: 1
Sobrante: 1
Spencer: 1
Square: 32
St: 41
st: 1
St.: 5
Stairway: 1
Steps: 2
street: 1
Street: 18728
Telegraph: 1
Terrace: 224
Trail: 1
Vallejo: 4
Walk: 15
Way: 1230
way: 1
Wedemeyer: 1
West: 10
Wharf: 2
"""