from math import *

# mach number is assumed to be the same even after engine failure. need to check this

a=[0]*100
b=[0]*100
e=[0]*100

f=open('input.txt','r')

i=0
for line in f:
    a[i]=line
    i+=1
    
j=0
while j<i:
    d,c,b[j]=str.partition(a[j],'=')
    j+=1

j=0


#~ while j<i:
    #~ b[j],c,d=str.partition(b[j],' ')
    #~ j+=1


j=0
while j<i:
	if (b[j].strip()== 'y' or b[j].strip()=="n"):
		j+=1
		continue 
	else:
		b[j]= float(b[j])
		j+=1

# Variable assigning

f_m=b[0]
M=b[1]
option=b[2].strip()
engine_dia=b[3]
ref_area=b[4]
engine_outer_dia=b[5]

# Calculating the wind milling drag

if option=='y':
    Cd_theory   = 0.46 - (0.0061*f_m) + (5.3125e-05 * (f_m**2)) - (0.46875e-06 * (f_m**3))

    c1          =0.3812917    
    c2          =-0.01033571
    c3          =0.1209066e-03
    c4          =-0.3640738e-06
    c5          =0.6598765
    c6          =-0.02579275
    c7          =0.2461761e-03
    c8          =-1.54045e-06
    c9          =-0.9736241
    c10         =0.04986446
    c11         =-0.7772863e-03
    c12         =5.087091e-06
    c13         =0.4385227
    c14         =-0.02264794
    c15         =0.3534701e-03
    c16         =-2.267849e-06

    delta_Cd= c1 + (c2*f_m) + ( c3*f_m**2) + ( c4*f_m**3) + (c5*M) + ( c6*M*f_m) + ( c7*M*f_m**2) + ( c8*M*f_m**3) + ( c9*M**2) + ( c10*M**2*f_m)+ (c11*M**2*f_m**2) + ( c12*M**2*f_m**3) + ( c13*M**3) + ( c14*M**3*f_m) + ( c15*M**3*f_m**2) + (c16*M**3*f_m**3)


if option =='n':

    if ( f_m>=20 and f_m<=46):
		Cd_theory= 0.2988+0.0091*f_m-0.32738e-03*f_m**2
    elif ( f_m> 46 and f<=80):
        Cd_theory=0.025


Cd_true= Cd_theory - delta_Cd

Cd= Cd_true*pi*engine_dia*engine_dia/(ref_area*4)

print 'windmilling drag is',Cd*10000,'counts'

Cd_spillage = 0.1*pi*engine_outer_dia*engine_outer_dia/(4*ref_area)
print 'spillage drag is',Cd_spillage*10000,'counts'
