# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:42:58 2017

@author: lippa2
"""

"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "map_sfo.osm"
#OSMFILE = "sample.osm"
#OSMFILE = "map.osm"
#OSMFILE = open("map.osm", "r")
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
city_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


# --- Cleaning Street
expected = ["Street", "Avenue", "Boulevard", "Drive", "Place", "Road", 
            "Highway", "East", "Broadway", "Place", "Way"]

mapping = { "St": "Street",
            "st": "Street",
            "St.": "Street",
            "street": "Street",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Rd.": "Road",
            "Ave": "Avenue",
            "AVE": "Avenue",
            "Ave.": "Avenue",
            "Hwy": "Highway",
            "Dr": "Drive",
            "E": "East",
            "broadway": "Broadway",
            "Pl": "Place", 
            "way": "Way"
            }

# --- Cleaning Street (Classcode)
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    try:
        m = street_type_re.search(name)
        if m.group() not in expected:
            if m.group() in mapping.keys():
                name = re.sub(m.group(), mapping[m.group()], name)
    except:
        name = None
    return name


def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"
# -----------------------------------------------------------------------------

# --- Cleaning City
city_expected = ["Alameda", "Albany", "Beach", "Berkeley", "Brisbane", "CA", 
                 "Emeryville", "Canyon", "Cerrito", "City", "Colma", "Francisco",
                 "Kensington", "Leandro", "Oakland", "Orinda", "Pacifica", "Piedmont",
                 "Richmond", "Sausalito", "Strawberry", "Tiburon", "Valley"]

city_mapping = { "Alamda": "Alameda",
                 "alameda": "Alameda",
                 "berkeley": "Berkeley",
                 "Emeyville": "Emeryville",
                 "oakland": "Oakland",
                 "OAKLAND": "Oakland",
                 "Okaland": "Oakland",
                 "ca": "CA"
                 }

def audit_city_type(city_types, city_name):
    m = city_type_re.search(city_name)
    if m:
        city_type = m.group()
        if city_type not in expected:
            city_types[city_type].add(city_name)

def is_city(city):
    return(city.attrib['k'] == "addr:city")

def audit_city(osmfile):
    osm_file = open(osmfile, "r")
    city_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_city_type(city_types, tag.attrib['v'])
    osm_file.close()
    return city_types


def update_city(name, city_mapping):
    try:
        m = city_type_re.search(name)
        if m.group() not in expected:
            if m.group() in mapping.keys():
                name = re.sub(m.group(), mapping[m.group()], name)
    except:
        name = None
        
    return name
# -----------------------------------------------------------------------------

# --- Clean up Postcodes
def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit_postcode(osmfile):
    osm_file = open(osmfile, "r")
    postcode = set()
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postcode(tag):
                    postcode.add(postcode, tag.attrib['v'])
    osm_file.close()
    return postcode

def update_postcode(postcode):
    #search = re.match(r'^\D*(\d{5}).*', postcode)
    #clean_postcode = search.group(1)
    try:
        search = re.match(r'^\D*(\d{5}).*', postcode)
        clean_postcode = search.group(1)
    except:
        clean_postcode = None
    
    return clean_postcode

bad_postcode = ['94103-3124', 'CA 94066', '94118-4504']

for i in bad_postcode:
    clean = update_postcode(i)
    print clean
    
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    test()
    
