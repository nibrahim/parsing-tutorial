# Exercise 12

import re
import sys

import utils


def parse_cmd():
    if len(sys.argv) != 2:
        print "Error. Specify input file."
        sys.exit(-1)
    return sys.argv[1]

def parse_partition(l):
    part, size =  l.split()
    size_re = re.compile('^([0-9]+) *([GMBK])?')
    if size != 'rest':
        m = size_re.search(size)
        size, unit = int(m.group(1)), m.group(2)
        size = utils.to_bytes(size, unit)
    return part, size
    
def parse_line(l):
    """
    All the regular lines are of the format K:V. This will parse and
    cleanup the lines, do appropriate type conversion and return the
    key and value.
    """
    if l.startswith("Partitions:"):
        return "Partitions", ""

    k,v = l.split(":")
    k = k.strip()
    v = v.strip()

    size_line_re = re.compile('^([0-9]+) *([GBMK])$')
    if k in ["Mem", "HDD Capacity"]: # These should be converted into bytes
        m = size_line_re.search(v)
        if m:
            g = m.groups()
            val, unit = int(g[0]), g[1]
            v = utils.to_bytes(val, unit)

    return k, v

def parse(filename):
    f = open(filename)
    ret = {}
    hostname = ""
    mdict = {}
    for line in f:
        line = utils.sanitise(line)
        if line:
            k,v = parse_line(line)
            if k == "hostname":
                # We're parsing a new machine now.  This means, that we've
                # finished parsing the previous one.  If we have something
                # already parsed, store it into the top level dictionary
                # and reset the machine dictionary
                if hostname:
                    ret[hostname] = mdict # Store everything parsed so far
                    mdict, hostname = {}, v # Reset
                else:
                    hostname = v
            elif k != "Partitions":
                # For everything other than partitions, we just store the value into
                # mdict
                mdict[k] = v
            else:
                part_dict = {}
                # For partitions, we parse separately till we encounter an empty line
                for part in f:
                    part = part.strip()
                    if not part:
                        break
                    partition, size = parse_partition(part)
                    if size == "rest":
                        total_size = mdict['HDD Capacity']
                        part_size = 0
                        for s in part_dict.values():
                            part_size += s
                        size = total_size - part_size
                    part_dict[partition] = size
                mdict['Partitions'] = part_dict
    # Put in the last machine
    ret[hostname] = mdict

    return ret

def main():
    filename = parse_cmd()
    import pprint
    pprint.pprint(parse(filename))
    

if __name__ == '__main__':
    main()
