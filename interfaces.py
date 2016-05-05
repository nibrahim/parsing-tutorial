# Exercise 13
import re

def parse_block(b):
    r = re.compile(r"inet addr:([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")
    interface_name = b.split()[0]
    m = r.search(b)
    if m:
        addr = m.groups()[0]
    else:
        addr = "no address"
    return interface_name, addr


    

# This loop breaks the input into 3 blocks
with open("interfaces.txt") as f:
    blocks = []
    block = []
    for line in f:
        if line.strip(): # Break at empty lines
            block.append(line.rstrip())
        else:
            blocks.append("\n".join(block))
            block = []

# Parse each block
for i in blocks:            
    iface, addr = parse_block(i)
    print "{:5} {}".format(iface, addr)
