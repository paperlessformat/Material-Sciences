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
for x in range(0, 360, 120):
    Ni_x = dist * cos(math.radians(x))
    Ni_y = dist * sin(math.radians(x))
    Ni_z = 0

    Ni = [Ni_x, Ni_y, Ni_z]
    print("Ni", str(Ni[0]), str(Ni[1]), str(Ni[2]))

#4th Ni
