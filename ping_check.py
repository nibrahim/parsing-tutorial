# Exercise 14

import subprocess

import utils


servers = ["google.com", "nonexistent.io", "qqqq.io", "facebook.com"]

for i in servers:
    op, err, retcode = utils.run_command(["ping", "-c", "1", i])
    if retcode != 0:
        print "{} is down".format(i)
    else:
        print "{} is up".format(i)
        
