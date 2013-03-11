from numpy import *

def readcolumn(file_name):
	kf_1=[0]*0;kf1_1=[0]*0;kf_2=[0]*0;kf1_2=[0]*0;kf_3=[0]*0;kf1_3=[0]*0;kf_4=[0]*0;kf1_4=[0]*0;kf_5=[0]*0;kf1_5=[0]*0;kf_6=[0]*0;kf1_6=[0]*0;kf_7=[0]*0;kf1_7=[0]*0
	kf_8=[0]*0;kf1_8=[0]*0
	
	for line in file(file_name):
		line = line.split()
		kf_1.append(line[0])
		kf1_1.append(line[1])
		kf_2.append(line[2])
		kf1_2.append(line[3])
		kf_3.append(line[4])
		kf1_3.append(line[5])
		kf_4.append(line[6])
		kf1_4.append(line[7])
		kf_5.append(line[8])
		kf1_5.append(line[9])
		kf_6.append(line[10])
		kf1_6.append(line[11])
		kf_7.append(line[12])
		kf1_7.append(line[13])
		kf_8.append(line[14])
		kf1_8.append(line[15])
		
		
	return kf_1,kf1_1,kf_2,kf1_2,kf_3,kf1_3,kf_4,kf1_4,kf_5,kf1_5,kf_6,kf1_6,kf_7,kf1_7,kf_8,kf1_8



if 1==1:
	kf_1=[0]*35
	akf_1=[0]*35
	kf1_1=[0]*35
	akf1_1=[0]*35
	kf_2=[0]*35
	akf_2=[0]*35
	kf1_2=[0]*35
	akf1_2=[0]*35
	kf_3=[0]*35
	akf_3=[0]*35
	kf1_3=[0]*35
	akf1_3=[0]*35
	kf_4=[0]*35
	akf_4=[0]*35
	kf1_4=[0]*35
	akf1_4=[0]*35
	kf_5=[0]*35
	akf_5=[0]*35
	kf1_5=[0]*35
	akf1_5=[0]*35
	kf_6=[0]*35
	akf_6=[0]*35
	kf1_6=[0]*35
	akf1_6=[0]*35
	kf_7=[0]*35
	akf_7=[0]*35
	kf1_7=[0]*35
	akf1_7=[0]*35
	kf_8=[0]*35
	akf_8=[0]*35
	kf1_8=[0]*35
	akf1_8=[0]*35



beta_A =3
A_tan_lambda_half=2
lamda = 0.7
eta0=0.5
etai=0.2

if beta_A >=1 and beta_A<2:
	
	if A_tan_lambda_half>=0 and A_tan_lambda_half<1:
		kf_1,kf1_1,kf_2,kf1_2,kf_3,kf1_3,kf_4,kf1_4,kf_5,kf1_5,kf_6,kf1_6,kf_7,kf1_7,kf_8,kf1_8= readcolumn('vortex_1.txt')
		akf_1,akf1_1,akf_2,akf1_2,akf_3,akf1_3,akf_4,akf1_4,akf_5,akf1_5,akf_6,akf1_6,akf_7,akf1_7,akf_8,akf1_8= readcolumn('vortex_2.txt')
		
		if lamda>=0 and lamda<0.125:
			
			if eta0>=0.3 and eta0<0.4:
				
				
				

	
