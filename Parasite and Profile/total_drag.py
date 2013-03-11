import os
from parasite_drag import *
from profile_drag import *
from numpy import *
from pylab import *

CD0_total,CD0_total_raymer= parasite_drag()
CDpminB,Kvisc,Clmin = profile_drag()

print CDpminB
print Clmin

Kvisc = 0.0424 #=1/pi*e*AR

CL = arange(0,1.3,0.1)
CD_profile = []
for i in range(len(CL)):
	CD_profile.append(CDpminB + Kvisc*((CL[i]-Clmin)**2))

CD = CD0_total + CD_profile

print CD0_total
print CD_profile 
#~ cd_actual = [0.014,0.015,0.016,0.018,0.021,0.025,0.03,0.035,0.04,0.047,0.054,0.061,0.067]
#~ 
#~ plot(CL,CL/CD)
#~ xlabel('C$_L$')
#~ ylabel('C$_L$/C$_D$')

plot(CD,CL)
xlabel('C$_D$')
ylabel('C$_L$')


legend(['Our code', 'Sample Data'])
grid()
show()


#~ plot(cd_actual,CL)
