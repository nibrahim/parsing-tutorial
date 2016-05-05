# Exercise 14

import subprocess

p = subprocess.Popen(["/usr/bin/whois", "cisco.com"], stdout = subprocess.PIPE)
for i in p.stdout:
    i = i.strip()
    if i.startswith("Registrant"):
        field, value = i.replace("Registrant ","").split(":")
        if value:
            print "{:15} {}".format(field, value)
