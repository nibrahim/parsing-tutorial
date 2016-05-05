total = 0
with open("numbers.txt") as f:
    for i in f:
        total += int(i)

print total
    
