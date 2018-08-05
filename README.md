# check-node-up
Puppet is performed to configure and OS hardening the node after the kickstart has been finished.
This script makes an API call to Puppet DB querying the last node check-in time in Puppet catalogue.
Compare the time with the current time to determine if the node has been up after the OS rebuild + latest OS patches.
