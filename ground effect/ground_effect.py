from math import *
from pylab import *

a=[0]*20
h=[0]*20
sigma=[0]*20
r=[0]*20
tau=[0]*20
delta_CL_total=[0]*20
delta_alpha=[0]*20
deltaCL=[0]*20
deltaCL_t = [0]*20
rat1=[0]*20
rat2=[0]*20
deltaCL_by_CL=[0]*20
e=[0]*20
f=[0]*20
g=[0]*20
phi=[0]*20
delta_CD=[0]*20
CD_new=[0]*20
l=[0]*20

z=open('input.txt','r')
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

# assigning the variables

A=a[0]
lift_slope=a[1]
CL=a[2]
#h =a[3]
b =a[4]
MAC=a[5]
t_by_c=a[6]
CD_p = a[7]
CD_v = a[8]

i=0
while i<20:
    h[i] = (i+1)*b/10.0
    i+=1


# calcuating sigma,r,tau and phi

for i in range (0,20):

    rat2[i] = h[i]/b
    sigma[i] = 2.7182818284590451**( -2.48*(2*rat2[i])**0.768)

    r[i]=sqrt(1+(2.0*rat2[i])**2) - 2.0*rat2[i]

    ratio=h[i]/MAC
    tau[i] = ratio/(8*pi*(ratio**2 + 1/64))

    phi[i]= 0.00066*( (570/rat2[i]) - 32/(rat2[i]**2) + (rat2[i])**(-3))
    

#calculating the change in lift

for i in range (0,20):
    e[i] = lift_slope*sigma[i]/(pi*A)
    f[i] = 1.0/(1 - e[i])
    g[i] = 1.0/((1 + tau[i]*CL*f[i])**2)

    deltaCL_by_CL[i] = f[i]*(e[i] + r[i]*(g[i]-1))
    
    deltaCL[i] = deltaCL_by_CL[i]*CL

    if CL<0.7 and (h[i]/MAC)<=1:
        delta_CL_t_0 = - (0.165*t_by_c**1.5)/(h[i]/MAC)**2.5
        deltaCL_t[i] = r[i]*(1-1.4*CL)*delta_CL_t_0
    else:
        deltaCL_t[i] =0

    delta_CL_total[i] = deltaCL[i] + deltaCL_t[i]

    delta_alpha [i] = - sigma[i]*CL/(pi*A)

for i in range(0,20):
    rat1[i] = (CL + delta_CL_total[i])/CL
    
plot(rat2,rat1, [0,2] , [1,1])
xlabel('h/b')
ylabel('C$_l(new)$/C$_l$')
grid()
show()
#print delta_CL_total
#print delta_alpha

# calculating the change in drag

for i in range(0,20):

    l[i] = (phi[i]*CL)/(pi * A)
    delta_CD[i] = -l[i]*CD_p - ( sigma[i] - ( 1-sigma[i])*l[i])*CD_v
    CD_new[i] = CD_p + CD_v + delta_CD[i]
    
plot( rat2, CD_new)
xlabel('h/b')
ylabel('C$_D(new)$/C$_D$')
#~ legend(['Our code', 'Sample Data'])
grid()
show()
print delta_CD




