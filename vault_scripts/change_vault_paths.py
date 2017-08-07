#!/usr/local/bin/python

import hvac
import sys

vault_address = 'https://vault.domain.com'
vault_token = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
client = hvac.Client(url=vault_address, token=vault_token)

envs = ['dev', 'staging']
services = [
  'audit-service',
  'auth-service',
  'backfill-service',
  'credit-service',
  'pull-service'
]

for env in envs:
  for service in services:
    old_secret_path = 'secret/' + service + '/' + env
    new_secret_path = 'secret/' + env + '/' + service
    current_secrets = client.read(old_secret_path)
    print 'Writing secrets for ' + new_secret_path
    client.write(new_secret_path, **current_secrets['data'])
    print ''


## Some earlier uneccessary attempts to create a formated string from the dict to pass to hvac

#def parse_secrets(current_secrets):
  #current_secrets = current_secrets["data"]
  #secrets_string = ', '.join('"%s":"%s"' % (key,val) for (key,val) in current_secrets.iteritems())
  #secrets_string = ', '.join("%s='%s'" % (key,val) for (key,val) in current_secrets.iteritems())
  #return secrets_string

#print(client.read('secret/auth-service/dev'))
#secrets_string = parse_secrets(current_secrets)
#for key, value in secrets.iteritems():
  #secrets_string = ':'.join([ key, value ])
  #secrets_string = '"' + key + '":"' + value + '"'
  #print secrets_string,
  #print key, ':', value
  #print ','.join(['"' + key + '":"' + value + '"']),

