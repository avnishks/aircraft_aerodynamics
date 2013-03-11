# height model of the atmoshere
from math import *
from numpy import *

def parasite_drag():
		
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
	
	parasite=[0]*100
	b=[0]*100
	
	
	f=open('master_input.txt','r')
	i=0
	for line in f:
		if not line.strip():
		   continue
		else:
			parasite[i]=line
			i+=1
	j=0
	while j<i:
		d,c,parasite[j]= str.partition(parasite[j],'=')
		if not parasite[j].strip():
			parasite[j]=0
		j+=1

	j=0
	while j<i:
		parasite[j]=float(parasite[j])
		j+=1
	f.close()

	# assigning variable names
	height							=parasite[0] 							
	M		 						=parasite[1] 														
	mac_wing					    =parasite[2]
	mac_ht                          =parasite[3]
	mac_vt                          =parasite[4]
	thick_rat_w	            		=parasite[5] 										
	length_rat_w		        	=parasite[6] 										
	thick_rat_ht	            	=parasite[7] 								
	length_rat_ht		    		=parasite[8] 							
	thick_rat_vt	            	=parasite[9] 							
	length_rat_vt		     		=parasite[10] 							
	sweep_angle_wing	     		=parasite[11] 							
	l_fuselage			        	=parasite[12]
	Amax							=parasite[13]
	l_nacelle						=parasite[14]
	A1max					    	=parasite[15]
	fuselage_wet			    	=parasite[16]
	wing_wet				    	=parasite[17]
	ht_wet					    	=parasite[18]
	vt_wet				        	=parasite[19]
	n_wet							=parasite[20]
	length_laminar_top_wing         =parasite[21]
	length_laminar_bottom_wing      =parasite[22]
	length_laminar_fuselage         =parasite[23]
	length_laminar_top_ht           =parasite[24]
	length_laminar_bottom_ht        =parasite[25]
	length_laminar_vt               =parasite[26]
	length_laminar_nacelle          =parasite[27]
	ref_area                        =parasite[28]
	sweep_angle_ht  	        	=parasite[29]
	sweep_angle_vt  	        	=parasite[30] 							

	# Calculation of air properties

	temp_inf,pressure_inf,rho_inf,mu_inf = height_model(height)
	a = sqrt(1.4*287*temp_inf)
	speed_inf = M*a

	# Calculation of reynolds number
	Re_f            = (rho_inf* speed_inf* l_fuselage*1.0)/mu_inf
	Re_w            = (rho_inf* speed_inf* mac_wing*1.0)/mu_inf
	Re_ht           = (rho_inf* speed_inf* mac_ht*1.0)/mu_inf
	Re_vt           = (rho_inf* speed_inf* mac_vt*1.0)/mu_inf
	Re_n            = (rho_inf* speed_inf* l_nacelle*1.0)/mu_inf

	# Calculation of laminar skin friction coefficient Cf_l for each component

	Cf_l_f          = 1.328/((Re_f)**0.5)
	Cf_l_w          = 1.328/((Re_w)**0.5)
	Cf_l_ht         = 1.328/((Re_ht)**0.5)
	Cf_l_vt         = 1.328/((Re_vt)**0.5)
	Cf_l_n          = 1.328/((Re_n)**0.5)

	# Calculation of turbulent skin friction coefficient Cf_t for each component

	Cf_t_f          =0.455/( ((log10(Re_f))**2.58)*((1+0.144*(M**2))**0.65))
	Cf_t_ht         =0.455/( ((log10(Re_ht))**2.58)*((1+0.144*(M**2))**0.65))
	Cf_t_w          =0.455/( ((log10(Re_w))**2.58)*((1+0.144*(M**2))**0.65))
	Cf_t_vt         =0.455/( ((log10(Re_vt))**2.58)*((1+0.144*(M**2))**0.65))
	Cf_t_n          =0.455/( ((log10(Re_n))**2.58)*((1+0.144*(M**2))**0.65))

	# Calculation of equivalent skin friction coefficient Cf for top and bottom surfaces by taking a weighted average

	Cf_f            = (length_laminar_fuselage* Cf_l_f)      + ((1-length_laminar_fuselage)*Cf_t_f)
	Cf_w_top        = (length_laminar_top_wing* Cf_l_w)      + ((1-length_laminar_top_wing)*Cf_t_w)
	Cf_w_bottom     = (length_laminar_bottom_wing* Cf_l_w)   + ((1-length_laminar_bottom_wing)*Cf_t_w)
	Cf_ht_top       = (length_laminar_top_ht* Cf_l_ht)       + ((1-length_laminar_top_ht)*Cf_t_ht)
	Cf_ht_bottom    = (length_laminar_bottom_ht* Cf_l_ht)    + ((1-length_laminar_bottom_ht)*Cf_t_ht)
	Cf_vt           = (length_laminar_vt*Cf_l_vt)            + ((1-length_laminar_vt)*Cf_t_vt)
	Cf_n            = (length_laminar_nacelle*Cf_l_n)        + ((1-length_laminar_nacelle)*Cf_t_n)

	# Calculation of raymer form factor

	a1              =1.34*(M**0.18)*(math.cos(sweep_angle_wing*pi/180))**0.28
	a2              =1.34*(M**0.18)*(math.cos(sweep_angle_ht*pi/180))**0.28
	a3              =1.34*(M**0.18)*(math.cos(sweep_angle_vt*pi/180))**0.28
	f_f             =l_fuselage/(math.sqrt(4*Amax/3.14))
	f_n             =l_nacelle/(math.sqrt(4*A1max/3.14))
	FF_w            =(1 + (0.6*thick_rat_w/length_rat_w) + 100*(thick_rat_w)**4)*a1
	FF_w = 1
	FF_ht           =((1 + (0.6*thick_rat_ht/length_rat_ht) + 100*(thick_rat_ht)**4)*a2)
	FF_vt           =((1 + (0.6*thick_rat_vt/length_rat_vt) + 100*(thick_rat_vt)**4)*a3)
	FF_f            =1+(60/((f_f)**3))+(f_f/400)
	FF_n            =1.5*(1+(0.35/f_n))

	# Calculation of skimenski form factor

	f_f_skimenski               = l_fuselage/(math.sqrt(4*Amax/3.14))
	f_n_skimenski               = l_nacelle/(math.sqrt(4*A1max/3.14))
	FF_f_skimenski              = 1 + 60/(f_f_skimenski)**3 + 0.0025*f_f_skimenski
	FF_n_skimenski              = 1 + 0.35/f_n_skimenski
	FF_w_skimenski              = 1 + 1.44*thick_rat_w + 2*(thick_rat_w)**2
	FF_ht_skimenski             = 1 + 1.44*thick_rat_ht + 2*(thick_rat_ht)**2
	FF_vt_skimenski             = 1 + 1.44*thick_rat_vt + 2*(thick_rat_vt)**2

	# Calculation of raymer interference factors

	Q_f             =1
	Q_w             =1
	Q_ht            =1.05
	Q_vt            =1.05
	Q_n             =1.2

	# Calculation of skimenski interference factors

	Q_f_skimenski             =1.02
	Q_w_skimenski             =1.2
	Q_ht_skimenski            =1.2
	Q_vt_skimenski            =1.17
	Q_n_skimenski             =1.3

	# Calculation of skimenski Cd0

	Cd0_f_skimenski           =(Cf_f*FF_f_skimenski*fuselage_wet*Q_f_skimenski )/ref_area
	Cd0_w_skimenski           =(((Cf_w_top+Cf_w_bottom)/2.0)*FF_w_skimenski*wing_wet*Q_w_skimenski)/ref_area
	Cd0_ht_skimenski          =(((Cf_ht_top+Cf_ht_bottom)/2.0)*FF_ht_skimenski*ht_wet*Q_ht_skimenski)/ref_area
	Cd0_vt_skimenski          =(Cf_vt*FF_vt_skimenski*vt_wet*Q_vt_skimenski)/ref_area
	Cd0_n_skimenski           =(Cf_n*FF_n_skimenski*n_wet*Q_n_skimenski)/ref_area
	Cd0_total_skimenski       =1.08*(Cd0_f_skimenski + Cd0_w_skimenski + Cd0_ht_skimenski + Cd0_vt_skimenski +Cd0_n_skimenski)
	
	
	# Calculation of raymer Cd0

	Cd0_f           =(Cf_f*FF_f*fuselage_wet*Q_f)/ref_area
	Cd0_w           =(((Cf_w_top+Cf_w_bottom)/2.0)*FF_w*wing_wet*Q_w)/ref_area
	Cd0_ht          =(((Cf_ht_top+Cf_ht_bottom)/2.0)*FF_ht*ht_wet*Q_ht)/ref_area
	Cd0_vt          =(Cf_vt*FF_vt*vt_wet*Q_vt)/ref_area
	Cd0_n           =(Cf_n*FF_n*n_wet*Q_n)/ref_area
	Cd0_total       =1.08*(Cd0_f + Cd0_w + Cd0_ht + Cd0_vt + Cd0_n)
	
	return Cd0_total_skimenski,Cd0_total


