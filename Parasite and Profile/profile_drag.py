from math import *

def profile_drag():
		
	a=[0]*100
	b=[0]*10
	Pj = [0]*15
	zj_root=[0]*15
	zj_tip=[0]*15

	def height_model(h):
		temp = -6.5*pow(10,-3) * h + 288.16
		pressure_rat = (temp/288.16)**(5.2532833020637906)
		pressure = 1.01325*(10**5) * pressure_rat
		density_rat = (temp/288.16)**(4.2532833020637906)	
		density = density_rat* 1.225
		a=1.458*10**-6 
		b = (temp**1.5)/(temp+110.4)
		mu=a*b
		return temp,pressure,density,mu


	z=open('master_input.txt','r')
	i=0
	for line in z:
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
	z.close()

	f= open('output_interpolation.txt','r')
	i=0
	for line in f:
		if not line.strip():
		   continue
		else:
			b[i]=line
			i+=1
	j=0
	while j<i:
		d,c,b[j]= str.partition(b[j],'=')
		if not b[j].strip():
			b[j]=0
		j+=1

	j=0
	while j<i:
		b[j]=float(b[j])
		j+=1
	f.close()

	# assigning the variables

	height 					= a[0]
	M						= a[1]
	x_tr 					= (a[21]+a[22])/2.0
	c						= a[31]
	c_bar 					= a[32]
	t_max					= a[33]
	t_75					= a[34]
	t_90					= a[35]
	lambda_quarter_chord	= a[36]
	epsilon1				= a[37]
	epsilon2				= a[38]
	kink_span 				= a[39]
	wing_span				= a[40]
	chord_root				= a[41]
	chord_kink				= a[42]
	chord_tip 				= a[43]
	lamda					= a[44]
	fuselage_radius			= a[45]
	aspect_ratio			= a[46]
	CL						= a[47]
	t_90_c					= a[48]
	t_99_c					= a[49]
	z92_by_z50_root			= a[50]
	z92_by_z50_tip			= a[51]
	
	for i in range(1,13):
		zj_root[i] = a[51+i]
	for i in range(1,13):
		zj_tip[i] = a[63+i]



	kc=b[0]
	km=b[1]
	a1w = b[2]
	KG =b[3]
	kv_root=b[4]
	km0_root=b[5]
	kv_tip=b[6]
	km0_tip=b[7]
	eta_ref=b[8]          
	alpha0r2 = b[9]  

	# Calculation of Re_c
	temp_inf,pressure_inf,rho_inf,mu_inf = height_model(height)
	a = sqrt(1.4*287*temp_inf)
	speed_inf = M*a
	Re_c = (rho_inf* speed_inf*c*1.0)/mu_inf

	# calculation of CDpmin0

	# calculation of CDmin at eta=0.5

	k1= (4.0 + (0.84*(8.5 - log10(Re_c))**2) - (3.4*x_tr) - (0.25*x_tr)*(8.5 - log10(Re_c))**2 )/1000
	k2= (8.46 + (1.15*(8.5 - log10(Re_c))**2) - (27.4*x_tr) - (3.97*x_tr)*(8.5 - log10(Re_c))**2 )/1000
	k3= (-0.29 - (0.12*(8.5 - log10(Re_c))**2) + (0.31*x_tr) - (0.12*x_tr)*(8.5 - log10(Re_c))**2 )/1000
	k4= (6.97 + (3.1*(8.5 - log10(Re_c))**2) + (16.6*x_tr) + (2.1*x_tr)*(8.5 - log10(Re_c))**2 )/1000

	Cd_min_th= k1 + (k2*t_max/c) + ( k3*t_75/t_max) + ( k4*t_max*t_75/(c*t_max))

	CDmin= Cd_min_th*kc*km

	# Calculation of CDf0 at eta=0.5

	te= t_max+5*t_90

	k5= (4.08 + 0.823*(8.5 - log10(Re_c))**2)/1000
	k6= (2.0 + 0.220*(8.5 - log10(Re_c))**2)/1000
	k7= (-3.67 - 0.343*(8.5 - log10(Re_c))**2)/1000
	k8= (-3.06 - 0.031*(8.5 - log10(Re_c))**2)/1000

	CDf0_M= k5*1.0 + k6*1.0*te/c + k7*1.0*x_tr + k8*1.0*x_tr*te/c

	km= 1 - ( 0.067 + 0.840*t_max/c )* M**2

	CDf0= CDf0_M* km

	# Calculation of CDpmin0

	CDpmin0 = (( CDmin - CDf0 )* (cos(lambda_quarter_chord*pi/180))**2) + CDf0

	# Calculation of profile drag due to geometric twist  CDpmin_epsilon

	epsilon_max= epsilon1*kink_span + epsilon2*(wing_span-kink_span)
	eta_max= 1
	span_2 = 0.2*wing_span
	span_8 = 0.8*wing_span


	if span_2<kink_span:
		epsilon_2 = epsilon1*span_2
	else:
		epsilon_2 = epsilon1*kink_span + epsilon2*(span_2-kink_span)

	if span_8<kink_span:
		epsilon_8 = epsilon1*span_8
	else:
		epsilon_8 = epsilon1*kink_span + epsilon2*(span_8-kink_span)

	Re_c_bar = 1.0*Re_c*c_bar/c

	K_Rc= 6.62 + 0.0743*(log10(Re_c_bar))**2 - 1.36*log10(Re_c_bar)
	CDpmin_epsilon = (1.2*KG*K_Rc*abs(epsilon_max)*eta_max*lamda*( abs(epsilon_2)+ abs(epsilon_8) ))/ ( 100000* (1 + lamda**2))
	CDpminB = CDpmin_epsilon + CDpmin0

	#print 'minimum profile drag/lift independent profile drag is',CDpminB*10000,'counts'

	# Calculating the viscous drag coefficient Kvisc

	#calculating the chord at the eta_ref

	eta_kink = 1.0*kink_span/wing_span

	if eta_ref<=eta_kink:
		chord_eta_ref = chord_root + ( chord_kink- chord_root)*(eta_ref*wing_span)/(kink_span)
	else:
		chord_eta_ref = chord_kink + ( chord_tip- chord_kink)*(eta_ref*wing_span - kink_span)/(wing_span-kink_span)


	Re_c_eta_ref = Re_c * chord_eta_ref/c

	tan_tau_aby2 = (t_90_c - t_99_c)/0.18
	timepass1 = 0.1 + (1.05-0.5*x_tr)*tan_tau_aby2
	timepass2 = (log10(Re_c_eta_ref) - 5)**(1 - 2.5*tan_tau_aby2)

	a0_by_a0t = 1 - 1.0*timepass1/timepass2

	Kvisc = (1.15/a1w)*(1-a0_by_a0t)
	#print 'The viscous drag coefficient is' ,Kvisc

	# Calculating the value of CLmin

	# calculating the value of zero lift alpha for aerofoil at eta_ref

	Pj[1]= -4.218
	Pj[2]= -3.129
	Pj[3]= -4.826
	Pj[4]= -5.879
	Pj[5]= -5.76
	Pj[6]= -6.254
	Pj[7]= -7.345
	Pj[8]= -9.381
	Pj[9]= -13.44
	Pj[10]= -23.517
	Pj[11]= -43.43
	Pj[12]= -199.618

	add2=0
	add3=0
	alpha0_root_inf=0
	alpha0_tip_inf=0
	for i in range(1,13):
		add2=Pj[i]*zj_root[i]
		add3=Pj[i]*zj_tip[i]
		alpha0_root_inf +=add2
		alpha0_tip_inf +=add3
		

	km_root = km0_root + (km0_root - 1 ) *log10(z92_by_z50_root)
	km_tip = km0_tip + (km0_tip - 1 )* log10(z92_by_z50_tip)

	alpha0_r = alpha0_root_inf*kv_root*km_root
	alpha0_t = alpha0_tip_inf*kv_tip*km_tip

	delta_t= epsilon1*kink_span + epsilon2*(wing_span-kink_span)
	delta_et= delta_t + alpha0_r - alpha0_t

	alpha0r_2 = delta_et*alpha0r2

	alpha0= 0.87*alpha0_root_inf + alpha0r_2

	a0t_by_a0= 1.0/a0_by_a0t
	alpha0_rads= alpha0*pi/180
	Clmin = (-1.21 * a1w * alpha0_rads )/( 1- (a0t_by_a0*a1w/(pi*aspect_ratio)))

	#print 'the Cl of the aircraft at minimum drag is',Clmin

	#~ CD_profile = CDpminB + Kvisc*((CL-Clmin)**2)
	#print ' the profile drag is' , CD_profile*10000

	return CDpminB,Kvisc,Clmin

