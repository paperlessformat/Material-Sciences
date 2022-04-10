#Generate Benzene.xyz file

import math
from math import cos
from math import sin

theta = range(0, 360, 60) 
r_CC = 1.39000
r_H = r_CC + 1.09000

print("12")
print("Benzene")

for x in theta:
    C_x = r_CC * cos(math.radians(x))
    C_y = r_CC * sin(math.radians(x))
    C_z = 0.00000

    H_x = r_H * cos(math.radians(x))
    H_y = r_H * sin(math.radians(x))
    H_z = 0.00000

    C = [C_x, C_y, C_z]
    H = [H_x, H_y, H_z]

    print("C", str((C[0])), str(C[1]), str(C[2]))
    print("H", str(H[0]), str(H[1]), str(H[2]))


