#!/usr/bin/env python

# s3_url_gen.py
# -------------
# This script takes two options, for bucket name and filename, and generates
# a url to open/download the file from s3. The url is good for 24 hours.
#
# example: ./s3_url_gen.py -b my_bucket -f my_file.png
#

import boto
import boto.s3.connection
import sys
import getopt

# Hardcoded values
s3_host = 'my_s3_host.amazonaws.com'
access_key = 'xxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxx'
expires = 86400    #in seconds

# Create connection to s3
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = s3_host,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

# Defining a function to print out script usage example
def usage():
   print 'Usage Example: ./s3_url_gen.py --bucket my_bucket --file my_file.png'

# Validating command line input with getopt
s3_file = None
s3_bucket = None

try:
  opts, args = getopt.getopt(sys.argv[1:],"b:f:",["bucket=", "file="])
except getopt.GetoptError:
  usage()
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-b", "--bucket"):
    s3_bucket =  arg
  elif opt in ("-f", "--file"):
    s3_file = arg
  else:
    usage()
    sys.exit(2)

# Verify a variables for bucket and file have been given
if s3_file is None or s3_bucket is None:
  usage()
  sys.exit(2)

# Generate the url
bucket = conn.get_bucket(s3_bucket)
file_key = bucket.get_key(s3_file)
file_url = file_key.generate_url(expires, query_auth=True, force_http=True)

# Print out the url
print file_url
