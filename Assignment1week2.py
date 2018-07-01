import re
s = input("enter the file name")
handle = open(s)
h = handle.read()
listi = re.findall('[0-9]+', h)
lent = len(listi)
sum = 0
for i in range(0, lent):
    sum += int(listi[i])
print(sum)
