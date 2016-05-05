# Exercise 13

with open("ping.txt") as f:
    for i in f:
        if i.startswith("rtt"):
            print i.split("/")[4]
