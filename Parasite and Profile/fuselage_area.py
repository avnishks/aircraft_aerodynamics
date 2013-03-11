
import math
a = 1.675
b = 1.505
length = 36.24

c = (1.0*(a-b)/(a+b))**2

d = 1 + (3*c)/(10 + math.sqrt(4-3*c))

circumference = math.pi*(a+b)*d 
area = circumference*length
print area
