#!/usr/bin/env python

import sys
import getopt
import boto
import os.path
from boto.s3.connection import S3Connection
from boto.s3.key import Key

aws_access_key_id = ''
aws_secret_access_key = ''
bucket = ''
filename = ''
path = ''

def usage():
    print 'Usage: ' + sys.argv[0] + ' -k "aws-access-key-id" -s "aws-secret-access-key" -b "bucket" -f "file" -p "path"'


if len(sys.argv) < 8:
    usage()
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:k:s:b:a:r:f:p:",["help", "aws-access-key-id=", "aws-secret-access-key=", "bucket=", "file=", "path="])
except getopt.GetoptError as e:
    usage()
    sys.exit(1)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit(1)
    elif opt in ("-k", "--aws-access-key-id"):
        aws_access_key_id = arg
    elif opt in ("-s", "--aws-secret-access-key"):
        aws_secret_access_key = arg
    elif opt in ("-b", "--bucket"):
        bucket = arg
    elif opt in ("-f", "--file"):
        filename = arg
    elif opt in ("-p", "--path"):
        path = arg

# Time to upload the file
try:
    destpath = os.path.join(path, filename)
    c = S3Connection(aws_access_key_id, aws_secret_access_key)
    b = c.get_bucket(bucket)
    k = Key(b)
    k.key = destpath
    k.set_contents_from_filename(filename)
    k.set_acl('bucket-owner-full-control')
except boto.exception as e:
    print "S3 exception: " + e
    sys.exit(1)

sys.exit(0)