from math import *

#______________________________________________________________________________________________________#
# Calculating the drag due to wheels

M=0.15
rho=1.16
mu=1.76e-05
temp=298
Re_w_crit=5e05
S=100
b_nose=0.652
dw_nose=0.560
Cd_by_Cd0_nose = 0.54
m_nose=0.26
n_nose=0.246
b_wing=1.050
dw_wing=0.966
Cd_by_Cd0_wing = 0.535
m_wing=0.403
n_wing=0.441

height_ground= 5

a= sqrt (1.4*287*temp)
Re_wheel_nose = (dw_nose * rho * M * a)/mu
Re_wheel_wing = (dw_wing * rho * M * a)/mu

if Re_wheel_nose> Re_w_crit:
    Cd0_nose = 0.65
else:
    Cd0_nose= 1.2

if Re_wheel_wing> Re_w_crit:
    Cd0_wing = 0.65
else:
    Cd0_wing= 1.2

if height_ground*1.0/dw_nose>1:
    p_nose=1
if height_ground*1.0/dw_wing>1:
    p_wing=1

Cd_wheel_nose = Cd_by_Cd0_nose*Cd0_nose*( b_nose*dw_nose- m_nose*n_nose)*p_nose/S
Cd_wheel_wing = Cd_by_Cd0_wing*Cd0_wing*( b_wing*dw_wing - m_wing*n_wing)*p_wing/S
print 'Cd nose wheel', Cd_wheel_nose*10000
print 'Cd wing wheel', Cd_wheel_wing*10000

#_______________________________________________________________________________________________________#
# Calculating the drag due to the struts

length_strut_wing=2.35
diameter_strut_wing=0.2
strut_inclination_wing = 0
#distance_strut_door_wing =
length_strut_nose=2.026
diameter_strut_nose=0.16
strut_inclination_nose = 0
#distance_strut_door_nose =
Cdsc = 1.2
R1_nose= (cos ( strut_inclination_nose*pi/180))**3
R2_nose= 1 
R3_nose= 1
R1_wing= (cos ( strut_inclination_wing*pi/180))**3
R2_wing= 1 
R3_wing= 1

Cd_strut_wing = (Cdsc* length_strut_wing*diameter_strut_wing*1.0*R1_wing*R2_wing*R3_wing)/ S
Cd_strut_nose = (Cdsc* length_strut_nose*diameter_strut_nose*1.0*R1_nose*R2_nose*R3_nose)/ S

print 'Cd wing strut', Cd_strut_wing*10000
print 'Cd nose strut', Cd_strut_nose*10000

#_______________________________________________________________________________________________________#
# Calculating the drag due to cavity

length_cavity_nose =2.5
width_cavity_nose = .75
Cdc_nose = 0.0301
length_cavity_wing =3.045
width_cavity_wing = 1.1
Cdc_wing = 0.030

Cd_cavity_wing = (Cdc_wing* length_cavity_wing*width_cavity_wing)/S
Cd_cavity_nose = (Cdc_nose* length_cavity_nose*width_cavity_nose)/S
Cd_cavity = Cd_cavity_nose + Cd_cavity_wing

print 'Cd cavity total',Cd_cavity*10000
print 'Cd cavity nose',Cd_cavity_nose*10000
print 'Cd cavity wing',Cd_cavity_wing*10000

#_______________________________________________________________________________________________________#
# Calculating the drag due to doors

thickness_door1 =1
thickness_door2 =1
thickness_door3 =1
width_door1 =1
width_door2 =1
width_door3 =1
CDd=1

Cd_door = CDd*( thickness_door1*width_door1 + thickness_door2 *width_door2 + thickness_door3 *width_door3)/ S
print 'Cd doors', Cd_door*10000
 

#_______________________________________________________________________________________________________#
# Calculating F1
t_by_c =0.130736543
Q=0.75

F1 = 1+Q*t_by_c
#~ print F1

#_______________________________________________________________________________________________________#
# Calculating F2

z_by_c=0.731272339
E=0.68
deflection_angle= 40

F2= ( 1 - (0.0186 - 0.018*( 0.5*z_by_c - 0.2) + 0.0053*((0.5*z_by_c-0.2)**2))*E*deflection_angle)**2
#~ print F2

#_______________________________________________________________________________________________________#
# Calculating the total drag

Cd_total = ( 2*Cd_wheel_wing + Cd_wheel_nose + 2*Cd_strut_wing + Cd_strut_nose + 3*Cd_cavity + Cd_door ) * F1 * F2

print 'total undercarriage Cd',Cd_total*10000

