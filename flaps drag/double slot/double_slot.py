from math import *
from pylab import *
f=open('input.txt','r')

a=[0]*25
i=0
for line in f:
    a[i]=line
    i+=1
j=0

while j<i:
    b,e,a[j]=str.partition(a[j],'=')
    j+=1
j=0
while j<i:
    a[j]=float(a[j])
    j+=1

# assigning variable names

extended_chord_ratio	        =a[0]
deflection_angle_1		=a[1]
deflection_angle_2		=a[2]
Cl1_prime       		=a[3]
Cl2_prime                       =a[4]
a1          			=a[5]
phi0_inboard                    =a[6]
phi1_inboard	                =a[7]
phi0_outboard		        =a[8]
phi1_outboard		        =a[9]

# calculating the values of Jt1 and Jt2

if deflection_angle_1<=23.5 and deflection_angle_1>=0:
    Jt1 = 1.17*(sin(3.83*pi/180*deflection_angle_1))**0.5
else:
    Jt1 = 1.17
    
if deflection_angle_1<=30 and deflection_angle_1>=(-10):
    Jt2 = 2.2 - 0.04*abs(deflection_angle_2)
else:
    Jt2 = 1.0

delta_CL0tw_inboard = extended_chord_ratio*( Jt1*Cl1_prime + Jt2*Cl2_prime)* (a1/(2*pi))* (phi1_inboard-phi0_inboard)
delta_CL0tw_outboard = extended_chord_ratio*( Jt1*Cl1_prime + Jt2*Cl2_prime)* (a1/(2*pi))* (phi1_outboard-phi0_outboard)

delta_CL0tw= delta_CL0tw_inboard+delta_CL0tw_outboard

print delta_CL0tw_inboard,delta_CL0tw_outboard,delta_CL0tw
