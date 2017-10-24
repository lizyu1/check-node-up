#!/usr/bin/python
# 23-10-2017 lyu14

import json
import sys


try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

USERNAME = "username"
PASSWORD = "password"
# Ignore SSL for now
SSL_VERIFY = False


def main(hostname):
    """
    Performs a GET using the passed URL location
    """

    r = requests.get('https://url/api/v2/hosts/{0}'.format(hostname), auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)

#    print r.text
    d = json.loads(r.content)
    id = d["id"]
    print id

if __name__ == "__main__":
    main(sys.argv[1])
