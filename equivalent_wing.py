from math import *

s0=10
s1=43.6044
s=96.25
cb=38.94
c1=21.06
ct=5.55
lambda0=25
xb=14052.89094
M=0.076549014

Se=((cb+c1)*(s1-s0) + (c1+ct)*(s-s1))*1.0
ln=xb*1.0
cr=(Se*1.0/(s-s0)) - ct
c0=((s*cr-s0*ct)/(s-s0))*1.0
lamda=ct*1.0/c0
c_bar=c0*(1+lamda)/2.0
A=2.0*s/c_bar
S=2.0*s*c_bar
#A=10.5
tan_lambda_half= tan(lambda0*pi/180) - (2.0*(1-lamda))/(A*(1+lamda))
lambda_half=atan(tan_lambda_half)
beta_a= A*((1-M**2)**0.5)
kappa= (1+2*lamda)/(3.0*(1+lamda))

mac = 2*cr*(1 + lamda + lamda**2)/3*(1+lamda)


print 'half wing sweep',lambda_half*180/pi, 'degrees'
print 'root chord', cr
print 'tip chord', ct
print 'sweep' , lambda0
print 'area', S
print 'AR', A
print 'MAC', mac
print 'BetaA', beta_a
print 'Atan(lamdba)', A*tan_lambda_half
print 'lamda',lamda
print 'taper parameter kappa', kappa
print lambda_half*180/pi
print c_bar
