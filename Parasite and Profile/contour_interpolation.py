from numpy import *
from scipy import *
from pylab import *
from scipy.interpolate import *
from matplotlib.pyplot import *

z_kc=[0]*90
Km_35_1 = [0]*35
Km_35_2 = [0]*20
Km_35_3 = [0]*24
Km_35_4 = [0]*42
Km_80_1 = [0]*35
Km_80_2 = [0]*20
Km_80_3 = [0]*36
Km_80_4 = [0]*30
a1w_1_by_A = [0]*91
a1w_2_by_A = [0]*91
a1w_3_by_A = [0]*91
a1w_4_by_A = [0]*91
a1w_5_by_A = [0]*91
KG=[0]*77
kv=[0]*121
km0 = [0]*77
eta_ref_1_array = [0]*80
eta_ref_2_1_array = [0]*12
eta_ref_2_2_array = [0]*80
eta_ref_3_1_array =[0]*70
eta_ref_3_2_array =[0]*90
eta_ref_4_1_array=[0]*70
eta_ref_4_2_array=[0]*60
eta_ref_5_1_array=[0]*50
eta_ref_5_2_array=[0]*80
eta_ref_6_1_array=[0]*12
eta_ref_6_2_array=[0]*80
alpha0r_1_array = [0]*20
alpha0r_2_array = [0]*20
alpha0r_3_array = [0]*20
alpha0r_4_array = [0]*20


M = 0.78
tm_by_c = 0.09
t_75_by_tm = 0.65
A_tan_lambda_half = 5.196
lamda = 0.3333
A = 10
tm_by_c_eta_5 = 0.11
logR_root = 6.9
logR_tip = 6.9
logz92_by_z50_root = -0.1
logz92_by_z50_tip    = -0.1
lambda_quarter = 23

beta_A = A*sqrt(1-M**2)

def readfile( file_name, quantity):
	f=open(file_name,'r')
	i=0
	for line in f:
		if not line.strip():
			continue
		else:
			quantity[i]=line
			i+=1
	j=0
	while j<i:
		quantity[j]=float(quantity[j])
		j+=1
	f.close()


def interpolate(x,y,z,xi,yi,type):
	
	X,Y = meshgrid(x,y)
	outgrid = interp2d( X,Y,z,kind=type)
	zi=outgrid(xi,yi)
	return zi



# digitizing the camber factor Kc from ESDU 00027
x_kc = [ 0,0.1,0.2,0.3,0.4,0.5,0.6,0.65,0.7,0.75]
y_kc = [0,0.5,1,1.5,2,2.5,3,3.5,4]
readfile('Kc_z.txt',z_kc)
c=0.7
d=3
Kc= interpolate(x_kc,y_kc,z_kc,c,d,'linear')
# print 'Kc =',Kc

# digitizing the mach number factor Km from ESDU 00027

if M>=0.5 and tm_by_c>=0.08:
	x_Km_35_1 = [ 0.5,0.6,0.65,0.7,0.75]
	y_Km_35_1 = [0.08,0.1,0.12,0.14,0.16,0.18,0.2]
	readfile('Km_35_1.txt',Km_35_1)
	Km_35 = interpolate( x_Km_35_1,y_Km_35_1, Km_35_1, M , tm_by_c,'linear')
	#print Km_35

if M>=0.5 and tm_by_c<0.08:
	x_Km_35_2 = [ 0.02,0.04,0.06,0.08]
	y_Km_35_2 = [0.5,0.6,0.65,0.7,0.75]
	readfile('Km_35_2.txt',Km_35_2)
	Km_35 = interpolate( x_Km_35_2,y_Km_35_2, Km_35_2,tm_by_c, M,'linear')
	#print Km_35

if M<0.5 and tm_by_c>=0.14:
	x_Km_35_3 = [ 0,0.1,0.2,0.3,0.4,0.5]
	y_Km_35_3= [0.14,0.16,0.18,0.2]
	readfile('Km_35_3.txt',Km_35_3)
	Km_35 = interpolate( x_Km_35_3,y_Km_35_3, Km_35_3, M , tm_by_c,'linear')
	#print Km_35

if M<0.5 and tm_by_c<0.14:
	y_Km_35_4 = [ 0.5,0.4,0.3,0.2,0.1,0]
	x_Km_35_4= [0.02,0.04,0.06,0.08,0.1,0.12,0.14]
	readfile('Km_35_4.txt',Km_35_4)
	Km_35 = interpolate( x_Km_35_4,y_Km_35_4, Km_35_4, tm_by_c, M,'linear' )
	#print Km_35

if M>=0.5 and tm_by_c>=0.08:
	x_Km_80_1 = [ 0.5,0.6,0.65,0.7,0.75]
	y_Km_80_1 = [0.08,0.1,0.12,0.14,0.16,0.18,0.2]
	readfile('Km_80_1.txt',Km_80_1)
	Km_80 = interpolate( x_Km_80_1,y_Km_80_1, Km_80_1, M , tm_by_c,'linear')
	#print Km_80

if M>=0.5 and tm_by_c<0.08:
	y_Km_80_2 = [ 0.02,0.04,0.06,0.08]
	x_Km_80_2 = [0.5,0.6,0.65,0.7,0.75]
	readfile('Km_80_2.txt',Km_80_2)
	Km_80 = interpolate( x_Km_80_2,y_Km_80_2, Km_80_2,M,tm_by_c,'cubic')
	#print Km_80

if M<0.5 and tm_by_c>=0.1:
	x_Km_80_3 = [ 0,0.1,0.2,0.3,0.4,0.5]
	y_Km_80_3= [0.1,0.12,0.14,0.16,0.18,0.2]
	readfile('Km_80_3.txt',Km_80_3)
	Km_80 = interpolate( x_Km_80_3,y_Km_80_3, Km_80_3, M , tm_by_c,'cubic')
	#print 'Km_80 =',Km_80
	
if M<0.5 and tm_by_c<0.1:
	y_Km_80_4 = [ 0.5,0.4,0.3,0.2,0.1,0]
	x_Km_80_4= [0.02,0.04,0.06,0.08,0.1]
	readfile('Km_80_4.txt',Km_80_4)
	Km_80 = interpolate( x_Km_80_4,y_Km_80_4, Km_80_4, tm_by_c, M ,'linear')
	#print Km_80
	


#interpolating for a given value of t0.75/tm
Km = Km_35 + (Km_80-Km_35)*(t_75_by_tm - 0.35)/0.45
#print 'Km =' , Km

# digitizing the lift curve slope a1w of the wing

if 1==1:   # just to make it collapsable, has no other purpose
	x_a1w = [6,5,4,3,2,1,0]
	y_a1w = [12,11,10,9,8,7,6,5,4,3,2,1,0]
	
	readfile('a1w_1.txt',a1w_1_by_A)
	a1w_0_by_A = interpolate(x_a1w,y_a1w,a1w_1_by_A,A_tan_lambda_half,beta_A,'linear')
	
	readfile('a1w_2.txt',a1w_2_by_A)
	a1w_125_by_A = interpolate(x_a1w,y_a1w,a1w_2_by_A,A_tan_lambda_half,beta_A,'linear')
	
	readfile('a1w_3.txt',a1w_3_by_A)
	a1w_250_by_A = interpolate(x_a1w,y_a1w,a1w_3_by_A,A_tan_lambda_half,beta_A,'linear')
	
	readfile('a1w_5.txt',a1w_5_by_A)
	a1w_1000_by_A = interpolate(x_a1w,y_a1w,a1w_5_by_A,A_tan_lambda_half,beta_A,'linear')
	
	readfile('a1w_4.txt',a1w_4_by_A)
	a1w_500_by_A = interpolate(x_a1w,y_a1w,a1w_4_by_A,A_tan_lambda_half,beta_A,'linear')
	
	

if lamda>0 and lamda<=0.125:
	a1w_by_A = a1w_0_by_A + (a1w_125_by_A - a1w_0_by_A)*lamda/0.125
if lamda>0.125 and lamda<=0.25:
	a1w_by_A = a1w_125_by_A + (a1w_250_by_A - a1w_125_by_A)*(lamda-0.125)/0.125
if lamda>0.25 and lamda<=0.5:
	a1w_by_A = a1w_250_by_A + ((a1w_500_by_A - a1w_250_by_A)*(lamda-0.25))/0.25
if lamda>0.5 and lamda<=1:
	a1w_by_A = a1w_500_by_A + (a1w_1000_by_A - a1w_500_by_A)*(lamda-0.5)/0.5

a1w =  a1w_by_A* A
#print 'a1w =', a1w

#interpolating the factor in twist of profile drag KG

x_KG = [ 2,3,4,5,6,7,8,9,10,11,12]
y_KG = [0.09,0.1,0.12,0.14,0.16,0.18,0.2]

readfile('KG.txt',KG)
KG= interpolate(x_KG,y_KG,KG,A,tm_by_c_eta_5,'cubic')
#print 'KG =', KG

#interpolating the zero lift angle of attack parameters kv and km0

x_kv = [6,6.2,6.4,6.6,6.8,7,7.2,7.4,7.6,7.8,8]
y_kv = [ 1,0.8,0.6,0.4,0.2,0,-0.2,-0.4,-0.6,-0.8,-1]
readfile('kv_aerofoil.txt',kv)
kv_root= interpolate(x_kv,y_kv,kv,logR_root,logz92_by_z50_root,'linear')
kv_tip= interpolate(x_kv,y_kv,kv,logR_tip,logz92_by_z50_tip,'linear')
#print 'kv of root =',kv_root
#print 'kv of tip=',kv_tip

x_km0 = x_kv
y_km0 = [ 0.6,0.5,0.4,0.3,0.2,0.1,0]
readfile('km0_aerofoil.txt',km0)
km0_root = interpolate(x_km0,y_km0,km0,logR_root,M,'cubic')
km0_tip = interpolate(x_km0,y_km0,km0,logR_tip,M,'cubic')

#print 'km0 of root=',km0_root
#print 'km0 of tip=',km0_tip 

# interpolating the reference section eta_ref

x_eta_ref_1 = [0,5,10,15,20,25,30,35,40,45]
y_eta_ref_1 = [12,10,8,6,4,3,2,1]

readfile('eta_ref_1.txt', eta_ref_1_array)
eta_ref_1 = interpolate(x_eta_ref_1,y_eta_ref_1,eta_ref_1_array,lambda_quarter,A,'linear')

#print eta_ref_1

if lambda_quarter>=30 and lambda_quarter<=45 and A>=1 and A<=3:
	x_eta_ref_2_1 = [ 30,35,40,45]
	y_eta_ref_2_1 = [ 1,2,3]
	readfile('eta_ref_2_1.txt', eta_ref_2_1_array)
	eta_ref_2 = interpolate(x_eta_ref_2_1,y_eta_ref_2_1,eta_ref_2_1_array,lambda_quarter,A,'linear')
	

else:
	x_eta_ref_2_2 = [0,5,10,15,20,25,30,35,40,45]
	y_eta_ref_2_2 = [12,10,8,6,4,3,2,1]
	readfile('eta_ref_2_2.txt', eta_ref_2_2_array)
	eta_ref_2 = interpolate(x_eta_ref_2_2,y_eta_ref_2_2,eta_ref_2_2_array,lambda_quarter,A,'linear')
	
#print eta_ref_2

if lambda_quarter>=0 and lambda_quarter<=45 and A>=1 and A<=4:
	x_eta_ref_3_1 = [1,1.5,2,2.5,3,3.5,4]
	y_eta_ref_3_1 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_3_1.txt', eta_ref_3_1_array)
	eta_ref_3 = interpolate(x_eta_ref_3_1,y_eta_ref_3_1,eta_ref_3_1_array,A,lambda_quarter,'linear')
	
else:
	x_eta_ref_3_2 = [ 12,11,10,9,8,7,6,5,4]
	y_eta_ref_3_2 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_3_2.txt', eta_ref_3_2_array)
	eta_ref_3 = interpolate(x_eta_ref_3_2,y_eta_ref_3_2,eta_ref_3_2_array,A,lambda_quarter,'linear')
	
	
#print eta_ref_3

if lambda_quarter>=0 and lambda_quarter<=45 and A>=6 and A<=12:
	y_eta_ref_4_1 = [12,11,10,9,8,7,6]
	x_eta_ref_4_1 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_4_1.txt', eta_ref_4_1_array)
	eta_ref_4 = interpolate(x_eta_ref_4_1,y_eta_ref_4_1,eta_ref_4_1_array,lambda_quarter,A,'linear')

else:
	y_eta_ref_4_2 = [1,2,3,4,5,6]
	x_eta_ref_4_2 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_4_2.txt', eta_ref_4_2_array)
	eta_ref_4 = interpolate(x_eta_ref_4_2,y_eta_ref_4_2,eta_ref_4_2_array,lambda_quarter,A,'linear')


#print eta_ref_4

if lambda_quarter>=0 and lambda_quarter<=45 and A>=8 and A<=12:
	y_eta_ref_5_1 = [12,11,10,9,8]
	x_eta_ref_5_1 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_5_1.txt', eta_ref_5_1_array)
	eta_ref_5 = interpolate(x_eta_ref_5_1,y_eta_ref_5_1,eta_ref_5_1_array,lambda_quarter,A,'linear')

else:
	y_eta_ref_5_2 = [1,2,3,4,5,6,7,8]
	x_eta_ref_5_2 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_5_2.txt', eta_ref_5_2_array)
	eta_ref_5 = interpolate(x_eta_ref_5_2,y_eta_ref_5_2,eta_ref_5_2_array,lambda_quarter,A,'linear')


#print eta_ref_5

if lambda_quarter>=30 and lambda_quarter<=45 and A>=10 and A<=12:
	y_eta_ref_6_1 = [12,11,10]
	x_eta_ref_6_1 = [30,35,40,45]
	readfile('eta_ref_6_1.txt', eta_ref_6_1_array)
	eta_ref_6 = interpolate(x_eta_ref_6_1,y_eta_ref_6_1,eta_ref_6_1_array,lambda_quarter,A,'linear')

else:
	y_eta_ref_6_2 = [1,2,3,4,6,8,10,12]
	x_eta_ref_6_2 = [0,5,10,15,20,25,30,35,40,45]
	readfile('eta_ref_6_2.txt', eta_ref_6_2_array)
	eta_ref_6 = interpolate(x_eta_ref_6_2,y_eta_ref_6_2,eta_ref_6_2_array,lambda_quarter,A,'linear')


#print eta_ref_6


#interpolating these values for the correct value of taper ratio lamda

if lamda>0.1 and lamda<=0.2:
	eta_ref = eta_ref_1 + (eta_ref_2 - eta_ref_1)*(lamda-0.1)/0.1
	
if lamda>0.2 and lamda<=0.4:
	eta_ref = eta_ref_2 + (eta_ref_3 - eta_ref_2)*(lamda-0.2)/0.2
	
if lamda>0.4 and lamda<=0.6:
	eta_ref = eta_ref_3 + (eta_ref_4 - eta_ref_3)*(lamda-0.4)/0.2

if lamda>0.6 and lamda<=0.8:
	eta_ref = eta_ref_4 + (eta_ref_5 - eta_ref_4)*(lamda-0.6)/0.2

if lamda>0.8 and lamda<=1:
	eta_ref = eta_ref_5 + (eta_ref_6 - eta_ref_5)*(lamda-0.8)/0.2

#print eta_ref

# intrepolating the ratio of the alpha0r_2 for finding zero lift angle of attack

A = 7.3
A_tan_lambda_quarter = 3.2

if 1==1:
	x_alpha0r_1 = [10,8,6,4,2]
	y_alpha0r_1 = [6,4,2,0]
	readfile('zero_lift_angle_1.txt',alpha0r_1_array)
	alpha0r_1 = interpolate(x_alpha0r_1,y_alpha0r_1,alpha0r_1_array,A,A_tan_lambda_quarter,'linear')

	x_alpha0r_2 = [6,4,2,0]
	y_alpha0r_2 = [2,4,6,8,10]
	readfile('zero_lift_angle_2.txt',alpha0r_2_array)
	alpha0r_2 = interpolate(x_alpha0r_2,y_alpha0r_2,alpha0r_2_array,A_tan_lambda_quarter,A,'linear')

	x_alpha0r_3 = [6,4,2,0]
	y_alpha0r_3 = [2,4,6,8,10]
	readfile('zero_lift_angle_3.txt',alpha0r_3_array)
	alpha0r_3 = interpolate(x_alpha0r_3,y_alpha0r_3,alpha0r_3_array,A_tan_lambda_quarter,A,'linear')

	x_alpha0r_4 = [6,4,2,0]
	y_alpha0r_4 = [2,4,6,8,10]
	readfile('zero_lift_angle_4.txt',alpha0r_4_array)
	alpha0r_4 = interpolate(x_alpha0r_4,y_alpha0r_4,alpha0r_4_array,A_tan_lambda_quarter,A,'linear')




#interpolating the above values for the correct value of lamda

if lamda>=0 and lamda<=0.25:
	alpha0r = alpha0r_1 + (alpha0r_2 - alpha0r_1)*(lamda)/0.25

if lamda>0.25 and lamda<=0.5:
	alpha0r = alpha0r_2 + (alpha0r_3 - alpha0r_2)*(lamda-0.25)/0.25
	
if lamda>=0.5 and lamda<=1:
	alpha0r = alpha0r_3 + (alpha0r_4 - alpha0r_3)*(lamda)/0.5
	


#writing variables into files
f= open('output_interpolation.txt','w')
value = 'Kc 		=' + str(float(Kc))
f.write(value + "\n")
f= open('output_interpolation.txt','a')
value = 'Km 		=' + str(float(Km))
f.write(value + "\n")
value = 'a1w 		=' + str(float(a1w))
f.write(value + "\n")
value = 'KG 		=' + str(float(KG))
f.write(value + "\n")
value = 'kv _root		=' + str(float(kv_root))
f.write(value + "\n")
value = 'km0_root 		=' + str(float(km0_root))
f.write(value + "\n")
value = 'kv _tip		=' + str(float(kv_tip))
f.write(value + "\n")
value = 'km0_tip 		=' + str(float(km0_tip))
f.write(value + "\n")
value = 'eta_ref 		=' + str(float(eta_ref))
f.write(value + "\n")
value = 'alpha0r 		=' + str(float(alpha0r))
f.write(value + "\n")
f.close()



