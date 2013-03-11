from math import *
from pylab import *
f=open('lift_input.txt','r')

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
Kf0				=a[1]
deflection_angle		=a[2]
Cl1_prime       		=a[3]
a1          			=a[4]
phi0_inboard                    =a[5]
phi1_inboard	                =a[6]
phi0_outboard		        =a[7]
phi1_outboard		        =a[8]
CL                              =a[9]

#  calculating CL0tw

if deflection_angle>=0 and deflection_angle<=23.5:

    Jt1= 1.17* ((sin ( 3.83*deflection_angle*pi/180))**0.5)

else:
    Jt1=1.17

CL0tw_inboard = extended_chord_ratio* Kf0 * Jt1 * Cl1_prime * a1 * ( phi1_inboard - phi0_inboard) / (2.0*pi)
CL0tw_outboard = extended_chord_ratio* Kf0 * Jt1 * Cl1_prime * a1 * ( phi1_outboard - phi0_outboard) / (2.0*pi)

CL0tw= CL0tw_inboard+CL0tw_outboard

CLmin= 0.10533
Kvisc=0.009328
CL_eff= 0.5*CL0tw+ CLmin - CL

print CL0tw_inboard,CL0tw_outboard
drag= Kvisc*CL_eff**2
print CL0tw,Jt1
print 'drag', drag*10000, 'counts'
