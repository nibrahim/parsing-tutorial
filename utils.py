GB = 1024.0 ** 3
MB = 1024.0 ** 2
KB = 1024.0 


def sanitise(line):
    line = line.strip()
    if "#" in line:
        comment_start = line.find("#")
        line = line[0:comment_start]
    return line.strip()

def to_bytes(val, unit):
    """ Receives a value and a unit (one of M, B, G or K) and returns
    the value in bytes"""

    if unit == "K":
        val *= KB
    elif unit == "M":
        val *= MB
    elif unit == "G":
        val *= GB
    return val

def humanise(num):
    if num > 1.5*GB:
        return round(num / GB, 2), "GB"
    elif 1.5*GB >= num > 1.5*MB:
        return round(num / MB, 2), "MB"
    elif 1.5*MB >= num > 1.5*KB:
        return round(num / KB, 2), "KB"
    else:
        return round(num, 2), "B"
