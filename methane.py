#Generate Methane.xyz file

import math
from math import cos
from math import sin

print("5")
print("Methane")

#First three Hydrogen Atoms
theta = range(0,360,120)
len = 1.08*cos(math.radians(19.47))
for x in theta:
    H_x = len*cos(math.radians(x))
    H_y = len*sin(math.radians(x))
    H_z = 0

    H = [H_x, H_y, H_z]
    print("H", str(H[0]), str(H[1]), str(H[2]))

#The Carbon Atom
h = 1.08*sin(math.radians(19.47))
C1 = [0, 0, h]

print("C", str((C1[0])), str(C1[1]), str(C1[2]))

#Last Hydrogren Atom

l = h + 1.08

H = [0, 0, l]