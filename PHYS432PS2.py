#!/usr/bin/env python
# coding: utf-8

# In[2]:


#code description
# author Natalie hardin
#date 02/12/2024

import numpy as np
import matplotlib.pyplot as plt

dt = 1
Nsteps = 100


# In[22]:


y_v = np.array([-1, 1, -1, 1])
x_v = np.array([-1, -1, 1, 1])
k_v = np.array([2, 2, 2, 2])

#setting up plot
plt.ion
fig, ax = plt.subplots(1,1)

#initial pos of vortices
p, = ax.plot(x_v, y_v, "o", markersize=10)

#initial velocity streamline
ngrid = 2
Y, X = np.mgrid[-ngrid:ngrid:40j, -ngrid:ngrid:40j]
vel_x = np.zeros(np.shape(Y))
vel_y = np.zeros(np.shape(Y))

#masking radius
r_mask = 1

#vortex loop
for i in range(len(x_v)):
    #iterate through each point in the mesh grid
    for m in range(len(vel_x)):
        for n in range(len(vel_y)):
            
    
    
ax.set_xlim([-ngrid, ngrid])
ax.set_ylim([-ngrid, ngrid])

ax.streamplot(X, Y, vel_x, vel_y, density=[1,1])

fig.canvas.draw()


# In[ ]:




