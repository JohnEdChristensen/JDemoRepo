import matplotlib.pyplot as plt
t1 = []
v1 = []
t2 = []
v2 = []
v0 = 4
P = 400
m = 70
dt = 0.1
N = 2000
C = 0.5
rho = 1.225
area = .33


def calculate(t,v,v0, P, m, dt, N, C, rho, area):
	v.append(v0 + ((P /(m * v0)) * dt) - (C * rho * area * (v0*v0)/(2 * m)) * dt)
	t.append(0)
	for i in range(0,N):
		v.append((v[i] +  (P /(m * v[i])) * dt) - (C * rho * area * (v[i]*v[i])/(2 * m)) * dt)
		t.append(t[i] + dt)



calculate(t1,v1,v0,P,m,dt,N,C,rho,area)
calculate(t2,v2,v0,P,m,dt,N,C,rho,0)
plt.plot(t1,v1,"r--",t2,v2,)
plt.ylabel('m/s')
plt.xlabel('time')
plt.axis([0,200,0,50])
plt.show()