import numpy as np
import matplotlib.pyplot as plt

R = 1
r_mag = R/np.sqrt(2)

theta = np.linspace(0,2*np.pi,num=200)
r_dir = np.array([np.cos(theta),np.sin(theta)])
r = r_mag*r_dir

x = np.linspace(-1,1,num=50)
x, y = np.meshgrid(x,x)
f = np.sqrt(R**2 - x**2 - y**2)

rho = r.copy()
rho.resize((3,200))
rho[2].fill(r_mag)

fig = plt.figure(figsize=(12,4))
fig.suptitle('Sphere',size=15)

ax1 = fig.add_subplot(1,3,(1,2), projection='3d')
ax1.set_title(r'$C:\; 45^\circ\mathrm{N}$ Line of Latitude')
ax1.plot_wireframe(x,y,f, color='tab:blue')
ax1.plot_wireframe(x,y,-f, color='tab:blue')
ax1.plot(*rho, ls='--', color='tab:red')

ax2 = fig.add_subplot(1,3,3)
ax2.set_title(r'$xy$-projection of $C$')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax2.grid()

ax2.plot(*r, ls='--', color='tab:red')

plt.show()