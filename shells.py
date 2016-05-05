# Exercise 13

shells = []
with open("/etc/shells") as f:
    for i in f:
        i = i.strip()
        if not i.startswith("#"):
            shells.append(i)

with open("/etc/passwd") as f:
    for i in f:
        i = i.strip()
        fields = i.split(":")
        name, shell = fields[0], fields[-1]
        if shell not in shells:
            print name
