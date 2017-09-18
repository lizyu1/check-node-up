import sys
import os
import calendar, time
import requests
import json

def main():
    #global timestamp
    
    unixboxisup = False

    while not unixboxisup:
        r = requests.get('http://<api>', auth=('user', 'pass'))
        # x = """{
        #         "cached_catalog_status": "not_used",
        #         "catalog_environment": "production",
        #         "catalog_timestamp": "2016-08-15T11:06:26.275Z",
        #         "certname": "greenserver.vm",
        #         "deactivated": null,
        #         "expired": null,
        #         "facts_environment": "production",
        #         "facts_timestamp": "2016-08-15T11:06:26.140Z",
        #         "latest_report_corrective_change": null,
        #         "latest_report_hash": "4a956674b016d95a7b77c99513ba26e4a744f8d1",
        #         "latest_report_noop": false,
        #         "latest_report_noop_pending": null,
        #         "latest_report_status": "changed",
        #         "report_environment": "production",
        #         "report_timestamp": "2016-08-15T11:06:18.393Z"
        #     }
        # """
        #d = json.loads(x)
        d = r.json.loads(r)
        timestamp_puppet = d["catalog_timestamp"]   # python ver 2.x
        print(timestamp_puppet)
        #timestamp_puppet = d["catalog_timestamp"].Value $ ??? python ver 3.x
        unixboxisup = checkboxisup(timestamp_puppet)


def checkboxisup(timestamp_puppet):

    utc_puppet = time.strptime(timestamp_puppet, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc_local = time.gmtime()

    epoch_puppet = calendar.timegm(utc_puppet)
    epoch_local = calendar.timegm(utc_local)

    print("epoch puppet ", epoch_puppet)
    print("epoch local  ", epoch_local)

    if epoch_puppet < epoch_local-1800:
        return False

    # print("unix box is up %s", (time.localtime))
    # print("unix box is up {0}".format(time.localtime))
    return True


# checkboxisup("2017-09-18T12:20:00.000Z")   # testing manualy

if __name__ == "__main__":
    # if len(sys.argv)!=2:
    #     print("Please pass unix UTC eg. '2017-09-18T12:20:00.000Z'")
    # else:
    #     main(sys.argv[1])
    #     #int("arg[0]={0}".format(sys.argv[0]))
    #     # print("arg[1]={0}".format(sys.argv[1]))
    #     # print(">>>>> len(sys.argv) = %i" % len(sys.argv))
        # pass
    main()
    

