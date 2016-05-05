# Exercise 07

import re
import sys

import utils


def parse_cmdline():
    if len(sys.argv[1:]) == 1:
        return sys.argv[1]
    else:
        print "Usage: sum.py numberlist"
        sys.exit(-1)

def sanitise(line):
    line = line.strip()
    if "#" in line:
        comment_start = line.find("#")
        line = line[0:comment_start]
    return line.strip()
    
def parse(line):
    num = re.compile(r'^([0-9]+)\s+([MGBKmgbk]?)$')
    match = num.search(line)
    if match:
        val, unit = match.groups()
        size_bytes = utils.to_bytes(int(val), unit)
        return size_bytes
    else:
        raise ValueError("Bad line '{}'".format(line))

def main():
    filename = parse_cmdline()
    total = 0
    with open(filename) as f:
        for i in f:
            i = sanitise(i)
            if i:
                try:
                    i = parse(i)
                    total += int(i)
                except ValueError as e:
                    print e

    val, unit = utils.humanise(total)
    print "{} {}".format(val, unit)


if __name__ == '__main__':
    main()
