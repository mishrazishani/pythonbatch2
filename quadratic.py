# TO Solve the quadratic equation ax**2 + bx + c = 0

import cmath

a = 2
b = 3
c = 4


# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
x = (-b-cmath.sqrt(d))/(2*a)
y = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(x,y))
