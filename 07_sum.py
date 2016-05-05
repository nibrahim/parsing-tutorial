# Exercise 08

import logging
import optparse
import re
import sys

import utils

logger = None

def setup_logging(debug):
    global logger
    logger = logging.getLogger("sum")
    logger.setLevel(logging.DEBUG)

    screen_handler = logging.StreamHandler()
    if debug:
        screen_handler.setLevel(logging.DEBUG)
    else:
        screen_handler.setLevel(logging.WARNING)
    screen_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    screen_handler.setFormatter(screen_formatter)

    file_handler = logging.FileHandler("sum.log", "w")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s")    
    file_handler.setFormatter(file_formatter)

    logger.addHandler(screen_handler)
    logger.addHandler(file_handler)

def parse_cmdline():
    "Makes sure that we have atleast one argument and returns it"
    parser = optparse.OptionParser(usage = "%prog [options] input_file")
    parser.add_option("-s", "--strict", 
                      help = "Abort if input file contains a bad line", 
                      action = "store_true",
                      default = False)
    parser.add_option("-d", "--debug", 
                      help = "Print verbose logs",
                      action = "store_true",
                      default = False)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error("Please provide a filename")
    return options, args[0]

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
    options, filename = parse_cmdline()
    setup_logging(options.debug)
    total = 0
    with open(filename) as f:
        for i in f:
            i = sanitise(i)
            if i:
                try:
                    logger.debug("Parsing %s", i)
                    i = parse(i)
                    total += int(i)
                except ValueError as e:
                    if options.strict:
                        logger.critical("%s Aborting", e)
                        sys.exit(-1)
                    else:
                        logger.warn("%s", e)

    val, unit = utils.humanise(total)
    print "{} {}".format(val, unit)


if __name__ == '__main__':
    main()
