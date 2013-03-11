# it is assumed that chord ratios of flaps and wings is constant
# the value of gamma is assumed to be constant
# the drag has been calculated for the individual cranks and been added

from math import *

a=[0]*100

f=open('input.txt','r')

i=0
for line in f:
    a[i]=line
    i+=1
j=0
while j<i:
    d,c,a[j]= str.partition(a[j],'=')
    j+=1

j=0
while j<i:
    a[j]=float(a[j])
    j+=1
    
# Assingnimg variables

inboard_chord_ratio         =a[0]
outboard_chord_ratio        =a[1]
inboard_delta_f             =a[2]
outboard_delta_f            =a[3] 	
inboard_gamma 		    =a[4]
outboard_gamma              =a[5]
lambda_unkink               =a[6]
lambda_kink                 =a[7]
inboard_span_end            =a[8]
outboard_span_end           =a[9]
inboard_span_start          =a[10]
outboard_span_start         =a[11]
wing_span                   =a[12]
unkink_taper_ratio          =a[13]
kink_taper_ratio            =a[14]


# calculating all angles in radians

inboard_gamma_rads= inboard_gamma* pi/180
outboard_gamma_rads= outboard_gamma* pi/180
inboard_delta_f_rads= inboard_delta_f* pi/180
outboard_delta_f_rads= outboard_delta_f* pi/180
lambda_unkink_rads= lambda_unkink* pi/180
lambda_kink_rads= lambda_kink* pi/180


# calculating the full span flap drag

Cd0_inboard = (1.29*((inboard_chord_ratio)**1.25)* ( ((sin(inboard_delta_f_rads+ inboard_gamma_rads))**2) - ((sin(inboard_gamma_rads))**2) ))*( cos(lambda_unkink_rads))
Cd0_outboard = 1.29*((outboard_chord_ratio)**1.25)* ( ((sin(outboard_delta_f_rads+ outboard_gamma_rads))**2) - ((sin(outboard_gamma_rads))**2))*( cos(lambda_kink_rads))

# calculating part span factor

mu1_inboard = ((inboard_span_end/wing_span)/(1+unkink_taper_ratio))*( 2- (inboard_span_end/wing_span)*( 1 - unkink_taper_ratio))
mu2_inboard = ((inboard_span_start/wing_span)/(1+unkink_taper_ratio))*( 2- (inboard_span_start/wing_span)*( 1 - unkink_taper_ratio))

mu1_outboard = ((outboard_span_end/wing_span)/(1+kink_taper_ratio))*( 2- (outboard_span_end/wing_span)*( 1 - kink_taper_ratio))
mu2_outboard = ((outboard_span_start/wing_span)/(1+kink_taper_ratio))*( 2- (outboard_span_start/wing_span)*( 1 - kink_taper_ratio))

mu_inboard= mu1_inboard-mu2_inboard
mu_outboard= mu1_outboard-mu2_outboard

# calculating the total drag

Cd_total = Cd0_inboard*mu_inboard + Cd0_outboard*mu_outboard
print Cd_total*10000, 'counts'

