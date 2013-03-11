from math import *
a=[0]*100

#f=open('f_20_s_15.txt','r')
#f=open('f_20_s_30.txt','r')
#f=open('f_20_s_45.txt','r')
#f=open('f_35_s_15.txt','r')
#f=open('f_35_s_30.txt','r')
#~ f=open('f_35_s_45.txt','r')
f=open('f_0_s_15.txt','r')
#f=open('f_0_s_30.txt','r')
#f=open('f_0_s_45.txt','r')

i=0
for line in f:
    if not line.strip():
       continue
    else:
        a[i]=line
        i+=1
j=0
while j<i:
    d,c,a[j]= str.partition(a[j],'=')
    if not a[j].strip():
        a[j]=0
    j+=1

j=0
while j<i:
    a[j]=float(a[j])
    j+=1
f.close()

# Assigning the variables

inboard_spoiler_plan_area       =a[0]
outboard_spoiler_plan_area      =a[1]
number_outboard_spoiler         =a[2]
outboard_spoiler_hinge_sweep    =a[3]
spoiler_deflection              =a[4]
wing_gross_area                 =a[5]
flap_frontal_area               =a[6]

# calculation of Cd0

outboard_spoiler_hinge_sweep_rads=a[3]*pi/180
spoiler_deflection_rads=a[4]*pi/180

spoiler_frontal_area= inboard_spoiler_plan_area*sin(spoiler_deflection_rads)+ number_outboard_spoiler*outboard_spoiler_plan_area*sin(spoiler_deflection_rads)*cos(outboard_spoiler_hinge_sweep_rads)

Cd0= (spoiler_frontal_area+flap_frontal_area)/wing_gross_area

print Cd0*10000,'counts'
               
