# Exercise 14

import re
import subprocess

import utils

p = subprocess.Popen(["/bin/df", "-kh"], stdout = subprocess.PIPE)
r = re.compile(r'([0-9.]+)([KGMB]?)')
total = 0
for i in p.stdout:
    i = i.strip()
    if i.startswith("Filesystem"):
        continue # Skip header line
    space = i.split()[3]
    v, u = r.search(space).groups()
    total += utils.to_bytes(float(v), u)

u,v = utils.humanise(total)
print "{} {}".format(u, v)
