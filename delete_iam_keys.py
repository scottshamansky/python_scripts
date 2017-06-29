#!/usr/bin/env python

# delete_iam_keys.py
# ------------------
# This script deletes an iam user's access keys. It takes one option, iam username.
#
# example: ./delete_iam_keys.py -u user-name
#

import boto
import sys
import getopt

# Hardcoded values
access_key = 'xxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxx'

# Creat connection to IAM
iam = boto.connect_iam(access_key, secret_key)

# Defining a function to print out script usage example
def usage():
  print 'Usage Example: ./delete_iam_keys.py --user user_name'

# Validating command line input with getopt
iam_user = None

try:
  opts, args = getopt.getopt(sys.argv[1:],"u:",["user="])
except getopt.GetoptError:
  usage()
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-u", "--user"):
    iam_user =  arg
  else:
    usage()
    sys.exit(2)

# Verify a variable for iam username was given
if iam_user is None:
  usage()
  sys.exit(2)

# Find all keys associated with a user, and delete them
data = iam.get_all_access_keys(user_name=iam_user)
for keys in data.list_access_keys_result.access_key_metadata:
    print 'Removing access key', (keys.access_key_id), 'for user', iam_user
    iam.delete_access_key(keys.access_key_id, iam_user)

