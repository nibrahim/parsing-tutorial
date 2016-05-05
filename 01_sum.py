import sys

def parse_cmdline():
    if len(sys.argv[1:]) == 1:
        return sys.argv[1]
    else:
        print "Usage: sum.py numberlist"
        sys.exit(-1)

def main():
    filename = parse_cmdline()
    total = 0
    with open(filename) as f:
        for i in f:
            total += int(i)

    print total


if __name__ == '__main__':
    main()
