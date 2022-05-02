#Method Brute Force

#Ni2
print("2")
print("Ni2")

D1 = [0, 0, 0]
D2 = [2.48, 0, 0]

print("Ni", str((D1[0])), str(D1[1]), str(D1[2]))
print("Ni", str((D2[0])), str(D2[1]), str(D2[2]))

#Ni3
import math
from math import cos
from math import sin

print("3")
print("Ni3")

dist = 2.48
for x in range(0, 360, 120):
    Ni_x = dist * cos(math.radians(x))
    Ni_y = dist * sin(math.radians(x))
    Ni_z = 0

    Ni = [Ni_x, Ni_y, Ni_z]
    print("Ni", str(Ni[0]), str(Ni[1]), str(Ni[2]))

#Ni4
print("4")
print("Ni4")

dist = 2.48
length = 2 * dist * sin(math.radians(60)) 

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)

#Ni5
print("5")
print("Ni5")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, 0, 0)

#Ni6
print("6")
print("Ni6")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, 0, 0)
print("Ni", dist, length, 0)

#Ni7
print("7")
print("Ni7")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, 0, 0)
print("Ni", dist, length, 0)
print("Ni", 2 * dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)

#Ni8
print("8")
print("Ni8")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", 0, dist, 0)
print("Ni", dist, dist, 0)
print("Ni", (dist * cos(math.radians(60))), dist + (dist * sin(math.radians(60))), 0)
print("Ni", dist + (dist * sin(math.radians(60))), (dist * cos(math.radians(60))), 0)
print("Ni", (dist * cos(math.radians(60))), -(dist * sin(math.radians(60))), 0)
print("Ni", -(dist * sin(math.radians(60))), (dist * cos(math.radians(60))), 0)

#Ni9
print("9")
print("Ni9")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, 0, 0)
print("Ni", 2 * dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, length, 0)
print("Ni", dist, length, 0)
print("Ni", 0, length, 0)

#Ni10
print("10")
print("Ni10")

print("Ni", 0, 0, 0)
print("Ni", dist, 0, 0)
print("Ni", dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)
print("Ni", dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, 0, 0)
print("Ni", 2 * dist + (dist * cos(math.radians(60))), dist * sin(math.radians(60)), 0)
print("Ni", 2 * dist, length, 0)
print("Ni", dist, length, 0)
print("Ni", 0, length, 0)
print("Ni", -dist * cos(math.radians(60)), dist * sin(math.radians(60)), 0)

#Ni3V
print("3")
print("Ni3")
print("Ni", 0, 0, 0)
print("Ni", 2.48, 0, 0)
print("Ni", 2 * 2.48, 0, 0)


#Ni4V
print("4")
print("Ni4")
print("Ni", 0, 0, 0)

dist = 2.48
length = 2 * dist * sin(math.radians(x))
for x in range(0, 360, 120):
    Ni_x = dist * cos(math.radians(x))
    Ni_y = dist * sin(math.radians(x))
    Ni_z = 0

    Ni = [Ni_x, Ni_y, Ni_z]
    print("Ni", str(Ni[0]), str(Ni[1]), str(Ni[2]))

#Ni5V
print("5")
print("Ni5")

dist = 2.48
h = dist * sin(math.radians(19))
for x in range(0, 360, 120):
    Ni_x = dist * cos(math.radians(x))
    Ni_y = dist * sin(math.radians(x))
    Ni_z = 0

    Ni = [Ni_x, Ni_y, Ni_z]
    print("Ni", str(Ni[0]), str(Ni[1]), str(Ni[2]))
print("Ni", 0, 0, h)
print("Ni", 0, 0, dist + h)

#Ni6V
print("6")
print("Ni6")

dist = 2.48

print("Ni", 0, 0, 0)
print("Ni", 0, 0, dist)

for x in range(0, 360, 120):
    Ni_x = dist * cos(math.radians(x))
    Ni_y = dist * sin(math.radians(x))
    Ni_z = dist

    Ni = [Ni_x, Ni_y, Ni_z]
    print("Ni", str(Ni[0]), str(Ni[1]), str(Ni[2]))

print("Ni", 0, 0, 2 * dist)

#Method GO
