
import math

# definitions
# spools - the spools on which the string is wound

# postfix of 1 and 2 refer to either spool or associated side of the robot

# r - radius of the spool
# l - horizontal distance between spool centers
# A - angle of spool measured from a reference point
#     (direction begin positive for extending)
#     the spools are wrapped in opposite directions
#     so that the string is on the outside
# B - smaller angle between string and horizontal
# C - smaller angle between tangent point and horizontal
# D - angle between d and f
# E - angle between f and horizontal

# d - distance from tangent point to carriage
# f - distance from spool center to carriage

l = 0.2
x = 0.1
y = 0.1

r1 = 0.01
r2 = 0.01

# given f

f1 = math.sqrt(x**2 + y**2)
f2 = math.sqrt((l - x)**2 + y**2)

E1 = math.atan(y / x)
E2 = math.atan(y / (l - x))

d1 = math.sqrt(f1**2 - r1**2)
d2 = math.sqrt(f2**2 - r2**2)

D1 = math.asin(r1 / f1)
D2 = math.asin(r2 / f2)

B1 = E1 - D1
B2 = E2 - D2

C1 = math.pi / 2.0 - B1
C2 = math.pi / 2.0 - B2


A1 = d1 / r1 + C1
A2 = d2 / r2 + C2




#tx1 = sx1 - r1 * math.cos(C1)
#ty1 = sy1 - r1 * math.sin(C1)

print A1, A2








