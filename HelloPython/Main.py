#!/usr/bin/env python3

fett = 23
print(fett)

a = 5
b = 13

maks = a if (a > b) else b

print(maks)

#x = float(input("1st Number: "))
#y = float(input("2nd Number: "))
#z = float(input("3rd Number: "))

#maximum = max((x, y, z))

#print("The maximal value is: " + str(maximum))

n = 100

s = 0
counter = 1
while counter <= n:
    s = s + counter
    print(s)
    counter += 1

print("Sum of 1 until %d: %d" % (n,s))

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

range(1, 10, 2)
print(list(range(1, 10, 2)))
