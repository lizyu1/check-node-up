# check-node-up
After the node has been finished its kickstart build, Puppet will be run to configure and perform OS hardening on the node.
This script makes an API call to Puppet DB querying the last check-in time of the node in Puppet catalogue.
Compare the time with the current time to determine if the node is up after the OS rebuild with the latest patches applied.
