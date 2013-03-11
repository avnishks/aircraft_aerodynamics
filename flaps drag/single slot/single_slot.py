a=[0]*100
c=[0]*100
t_max=[0]*100
t_75=[0]*100
Re_c=[0]*100
Cd_min_th=[0]*100
cdpmin =[0]*100
Km_35 =[0]*100
Km_80=[0]*100
Km =[0]*100
CdpminB=[0]*100

# the integration has been done assuming a  constant CD and taking its average value
from math import *
f=open('input.txt','r')

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

speed			        =a[0]
rho				=a[1]
mu				=a[2]
root_chord			=a[3]
kink_chord			=a[4]
tip_chord                       =a[5]
x_tr		                =a[6]
thick_root		        =a[7]
thick_kink		        =a[8]
thick_tip		        =a[9]
thick_75c_root		        =a[10]
thick_75c_kink	                =a[11]
thick_75c_tip	                =a[12]
kink_span                       =a[13]
unkink_span                     =a[14]
Km_35_root                      =a[15]
Km_35_kink                      =a[16]
Km_35_tip                       =a[17]
Km_80_root                      =a[18]
Km_80_kink                      =a[19]
Km_80_tip                       =a[20]
Kc                              =a[21]
extended_chord_ratio            =a[22]
Cd_prime_pmindelta              =a[23]
y2                      	=a[24]
y4                              =a[25]
y1                              =a[26]
y3                              =a[27]
wing_span 			=a[28]
quarter_chord_sweep_unkink	=a[29]
quarter_chord_sweep_kink	=a[30]
ref_area		        =a[31]
y0                              =a[32]

# interpolating chord

c[0]=root_chord
j=1

while j<11:
    c[j]= root_chord + (kink_chord-root_chord)*j/10
    j+=1
j=1
while j<25:
    c[10+j]= kink_chord + ( tip_chord-kink_chord)*j/25
    j+=1


# interpolating max thickness

t_max[0]=thick_root
j=1

while j<11:
    t_max[j]= thick_root + (thick_kink-thick_root)*j/10
    j+=1
j=1
while j<25:
    t_max[10+j]= thick_kink + ( thick_tip-thick_kink)*j/25
    j+=1

# interpolating thickness at 0.75c

t_75[0]=thick_75c_root
j=1

while j<11:
    t_75[j]= thick_75c_root + (thick_75c_kink-thick_75c_root)*j/10
    j+=1
j=1
while j<25:
    t_75[10+j]= thick_75c_kink + ( thick_75c_tip-thick_75c_kink)*j/25
    j+=1

# calculating the reynolds number for various sections
i=0
while i<35:
    Re_c[i]= rho*speed*c[i]/(mu*1000)
    i+=1
# calculatng minimum parasite drag CDpminB

i=0

while i<35:

    k1= (4.0 + (0.84*(8.5 - log10(Re_c[i]))**2) - (3.4*x_tr/c[i]) - (0.25*x_tr/c[i])*(8.5 - log10(Re_c[i]))**2 )/1000
    k2= (8.46 + (1.15*(8.5 - log10(Re_c[i]))**2) - (27.4*x_tr/c[i]) - (3.97*x_tr/c[i])*(8.5 - log10(Re_c[i]))**2 )/1000
    k3= (-0.29 - (0.12*(8.5 - log10(Re_c[i]))**2) + (0.31*x_tr/c[i]) - (0.12*x_tr/c[i])*(8.5 - log10(Re_c[i]))**2 )/1000
    k4= (6.97 + (3.1*(8.5 - log10(Re_c[i]))**2) + (16.6*x_tr/c[i]) + (2.1*x_tr/c[i])*(8.5 - log10(Re_c[i]))**2 )/1000

    Cd_min_th[i] = k1 + (k2*t_max[i]/c[i]) + ( k3*t_75[i]/t_max[i] ) + ( k4*t_max[i]*t_75[i]/(c[i]*t_max[i]))
    i+=1

i=0
while i<11:
    Km_35[i] = Km_35_root + (Km_35_kink-Km_35_root)*i/10
    i+=1

i=1
while i<25:
    Km_35[10+i] = Km_35_kink + (Km_35_tip-Km_35_kink)*i/25
    i+=1

i=0
while i<11:
    Km_80[i] = Km_80_root + (Km_80_kink-Km_80_root)*i/10
    i+=1

i=1
while i<25:
    Km_80[10+i] = Km_80_kink + (Km_80_tip-Km_80_kink)*i/25
    i+=1

i=0

while i<35:
    Km[i]= Km_35[i] + (Km_80[i]-Km_35[i])*(t_75[i]/t_max[i])/0.45
    i+=1

i=0
while i<35:
    CdpminB[i]= Cd_min_th[i]*Km[i]*Kc
    i+=1

Cdpmindelta= Cd_prime_pmindelta* extended_chord_ratio


i=0
while i<35:
    cdpmin[i]= Cdpmindelta + CdpminB[i]*( extended_chord_ratio-1)
    i+=1


# calculating the average value
i=0
add=0
while i<35 and cdpmin!=0:
   add+=cdpmin[i]
   i+=1
cdpmin_avg=add*1.0/i

# integrating this value over the span with the flaps to find complete Cd

inboard_chord_start = root_chord - ((root_chord-kink_chord)/kink_span)*(y1-y0)
inboard_chord_end = root_chord - ((root_chord-kink_chord)/kink_span)*(y2-y0)
outboard_chord_start = kink_chord - ((kink_chord-tip_chord)/unkink_span)*(y3-kink_span-y0)
outboard_chord_end = kink_chord - ((kink_chord-tip_chord)/unkink_span)*(y4-kink_span-y0)

A1= 0.5* (inboard_chord_start+ inboard_chord_end)*(y2-y1)/1000000
A2= 0.5* (outboard_chord_start+ outboard_chord_end)*(y4-y3)/1000000

Cdp_total = (2*0.9*cdpmin_avg)*( (A1*cos(quarter_chord_sweep_unkink*pi/180) + A2*cos(quarter_chord_sweep_kink*pi/180)))/ref_area

print Cdp_total*10000, 'counts'
