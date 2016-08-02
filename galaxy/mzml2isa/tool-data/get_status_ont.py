import sys
import os
import json
import urllib.error
import urllib.request as rq
from urllib.parse import quote
import csv 

###############################################################################
# Python3 script to get tab seperated maf_index.loc files for drop down menus
###############################################################################
# Code modified from mzm2isa-qt python package developed by Martin Larralde
# https://github.com/althonos/mzml2isa-qt/scrapers.py


def get_ont_loc(jsonSourceUrl, sparName, ontoClass, filepth):
    onto = json.loads(rq.urlopen(jsonSourceUrl).read().decode('utf-8'))
    info = []
    for x in onto:
        if '@type' in x:
            if ontoClass in x['@type']:
                info.append(x)
    info = [ (x['http://www.w3.org/2000/01/rdf-schema#label'],x['@id']) for x in info ]

    ontd  = {x[0]['@value'].capitalize():y for (x,y) in info}

    with open(filepth, 'w') as f:
        writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_ALL)
        writer.writerow(["name", "link"])
        for key, value in ontd.items():
            writer.writerow([key, value])

    return ontd

#-------------------------------
# publication status ontology
#-------------------------------
jsonSourceUrl = "http://www.sparontologies.net/ontologies/pso/source.json"
sparName = "pso"
ontoClass = "http://purl.org/spar/pso/PublicationStatus"
get_ont_loc(jsonSourceUrl, sparName, ontoClass, './pub_status.loc')

#-------------------------------
# Job role ontology
#-------------------------------
jsonSourceUrl = "http://www.sparontologies.net/ontologies/pro/source.json"
sparName = "pro"
ontoClass = "http://purl.org/spar/pro/PublishingRole"
get_ont_loc(jsonSourceUrl, sparName, ontoClass, './pub_role.loc')


