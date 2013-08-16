#!/usr/bin/python
# What: Snippet to include Shodan input to an ETL process. Reads a list of IP addresses and generates a json file with Shodan's output.
# POC: ewhyne@data-tactics.com 
# License: Open Source Software - Apache2

from shodan import WebAPI
import json

SHODAN_API_KEY = "your api key"
infilename = "hosts.txt" # one ip per line
outfilename = "output.json"

shodan = WebAPI(SHODAN_API_KEY)

print "Reading hosts from ", infilename
print "Writing json to ", outfilename, "\n"

outfile = open(outfilename, 'w')
for line in open(infilename, 'r'):
    print "Looking up ", line
    host = shodan.host(line)
    outfile.write(json.dumps(host, indent=4))
outfile.close




