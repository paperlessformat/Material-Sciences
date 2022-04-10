#Generate Ethane.xyz file

import math
from math import cos
from math import sin

print("8")
print("Ethane")

#First three Hydrogen Atoms
theta1 = range(0,360,120)
len = 102.02/100
for x in theta1:
    H_x = len*cos(math.radians(x))
    H_y = len*sin(math.radians(x))
    H_z = 0

    H = [H_x, H_y, H_z]
    print("H", str(H[0]), str(H[1]), str(H[2]))

#The two Carbon Atoms
h = 39.51/100
C1 = [0, 0, h]

print("C", str((C1[0])), str(C1[1]), str(C1[2]))

r_CC = 153.51/100
C2 = [0, 0, r_CC + h]

print("C", str((C2[0])), str(C2[1]), str(C2[2]))

#Last three Hydrogen Atoms
theta2 = range(60,420,120)
for x in theta2:
    H_x = len*cos(math.radians(x))
    H_y = len*sin(math.radians(x))
    H_z = r_CC + 2*h

    H = [H_x, H_y, H_z]
    print("H", str(H[0]), str(H[1]), str(H[2]))