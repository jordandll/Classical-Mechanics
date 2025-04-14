import numpy as np
import matplotlib.pyplot as plt

# Define parameters.
R = 1
r_mag = R/np.sqrt(2)

# Define domain of position vector(s).
theta = np.linspace(0,2*np.pi,num=200)

r_dir = np.array([np.cos(theta),np.sin(theta)])
r = r_mag*r_dir

# Define domain of sphere giving functions.
x = np.linspace(-1,1,num=50)
x, y = np.meshgrid(x,x)
f = np.sqrt(R**2 - x**2 - y**2)

# Define positon vector.
rho = r.copy()
rho.resize((3,200))
rho[2].fill(r_mag)

rho_x = r_mag*(np.cos(theta)-1)/np.sqrt(2)
rho_y = r_mag*np.sin(theta)
rho_z = r_mag*(np.cos(theta)+1)/np.sqrt(2)
p = rho = np.array([rho_x,rho_y,rho_z])

# Create Figure.
fig = plt.figure(figsize=(4,4))
fig.suptitle('Tilted Sphere',size=15)

ax = fig.add_subplot(1,1,1, projection='3d')
ax.set_title(r"$C':\;45^\circ\mathrm{N}$ Line of Latitude")

ax.plot(*p, ls='--', color='tab:red')

plt.show()
