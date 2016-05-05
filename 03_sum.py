# Exercise 04 and 05

import sys

def humanise(num):
    GB = 1024.0 ** 3
    MB = 1024.0 ** 2
    KB = 1024.0 

    if num > 1.5*GB:
        return round(num / GB, 2), "GB"
    elif 1.5*GB >= num > 1.5*MB:
        return round(num / MB, 2), "MB"
    elif 1.5*MB >= num > 1.5*KB:
        return round(num / KB, 2), "KB"
    else:
        return round(num, 2), "B"

def parse_cmdline():
    if len(sys.argv[1:]) == 1:
        return sys.argv[1]
    else:
        print "Usage: sum.py numberlist"
        sys.exit(-1)

def parse(line):
    line = line.strip()
    if "#" in line:
        comment_start = line.find("#")
        line = line[0:comment_start]
    return line

def main():
    filename = parse_cmdline()
    total = 0
    with open(filename) as f:
        for i in f:
            i = parse(i)
            if i:
                total += int(i)

    val, unit = humanise(total)
    print "{} {}".format(val, unit)


if __name__ == '__main__':
    main()
