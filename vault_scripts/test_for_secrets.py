#!/usr/local/bin/python

# test_for_secrets.py
# ------------------
# This script checks the plain text-configs files for secrets matching a regex list
# and prints them out for verification/testing.
#
# example: ./test_for_secrets.py -e dev -m auth-service
#

import getopt
import os
import sys
import re

microservice = None
environment = None
base_path = '/path/to/config/files'
regexlist = [
  "(.*)(P|p)assword(=| =)(.*)",
  "(.*)secret(=| =)(.*)",
  "(.*)pw(=| =)(.*)",
  "(.*)api(-|.|)key(=| =)(.*)",
  "(.*)access.key(=| =)(.*)",
  "(.*)secret.key(=| =)(.*)",
  "(.*)(U|u)ser(name|)(=| =)(.*)",
  "(.*)(private|public)key.name(=| =)(.*)",
  "(.*)oauth.client-id(=| =)(.*)",
  "(.*)chrome.api.account-number(=| =)(.*)"
  ]

# Usage statement
def usage():
  print 'Usage example: test_for_secrets.py -e dev -m auth-service'

# Validating command line input with getopt
try:
  opts, args = getopt.getopt(sys.argv[1:],"m:e:",["microservice=", "environment="])
except getopt.GetoptError:
  usage()
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-m", "--microservice"):
    microservice = arg
  elif opt in ("-e", "--environment"):
    environment = arg
  else:
    usage()
    sys.exit(2)

# Check variables
if microservice is None or environment is None:
  usage()
  sys.exit(2)

# Search each line of the file for regex match and print out results
config_file = base_path + microservice + '/' + microservice + '-' + environment + '.properties'
configs = open(config_file, "r")           # open file for reading
for line in configs:                       # for each line in the file...
  for regex in regexlist:                  # for each line in the regex list...
    if not line.strip().startswith("#"):   # strip out blank lines and commented lines
      if re.match(regex, line):            # if line matches regex list...
        print line,                        # print it

