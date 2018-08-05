
import sys
import os
import calendar, time
import requests
import json


def main(nodename):
    ''' request puppet node catalog_timestamp
        on success, check node up within last 30 mins
    ''' 
    
    while True:
        try:
            r = requests.get('http://abcd.tv/{0}'.format(nodename), timeout=1, auth=('user', 'pass'))
            r.raise_for_status()
            if r.status_code == 200:
                d = r.json.loads(r)
                timestamp_puppet = d["catalog_timestamp"]
                if comparetimestamp(timestamp_puppet):
                    dowork()
                    break
        except requests.exceptions.HTTPError as err:
            print err
        except requests.exceptions.RequestException as e:
            print e
        time.sleep(15)


def comparetimestamp(timestamp_puppet):
    ''' success == node up within last 30 mins
    ''' 

    utc_puppet = time.strptime(timestamp_puppet, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc_local = time.gmtime()

    epoch_puppet = calendar.timegm(utc_puppet)
    epoch_local = calendar.timegm(utc_local)

    return epoch_puppet > epoch_local-1800


def dowork():
    print "node is up"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        scriptname = sys.argv[0].split('/')[:-1]
        print("Usage: {0} <hostname>".format(scriptname))

    
