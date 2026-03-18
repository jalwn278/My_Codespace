import matplotlib.pyplot as plt
import numpy as np
def calBombTrace(h,v0):
    g=9.8
    tmax=(2*h/g)**0.5
    t=np.linspace(0,tmax)
    xt=v0*t
    yt=h-1/2*g*t**2
    return xt,yt

H=[3000,2000,1800]
V0=[200,260,300]
for h in H:
    for v in V0:
        xt,yt=calBombTrace(h,v)
        plt.plot(xt,yt)
plt.grid('on')
plt.axis([0,6500,0,3000])
plt.show()

#T=np.linspace(0,tmax,n)
#xt=[v0*t for t in T]
#yt=[h-1/2*g*t**2 for t in T]

#T=[i*delta for i in range(n)]
#xt=[v0*t for t in T]
#yt=[h-1/2*g*t**2 for t in T]

#while语句
#while 0<=t<=tmax:
 #   xt.append(v0*t)
 #  yt.append(h-1/2*g*t**2)
 #   t=t+delta

#也可用for语句 for i in range(n):
#                  t=t*i
#                  xt.append(v0*t)
#                  yt.append(h-1/2*g*t**2)