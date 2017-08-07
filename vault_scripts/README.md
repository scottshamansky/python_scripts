# Vault Scripts

A few scripts that I used for bulk reading/writing of secrets to Hashicorp's Vault. These are very environment specific, but good for some python examples

* change_vault_paths.py - example of bulk updating secrets paths using the hvac python client to read and re-write secrets...  in this case swapping two elements of the path around
* test_for_secrets.py - example of reading a plain text config file, looking for matches from a regex list, and printing those matching lines

