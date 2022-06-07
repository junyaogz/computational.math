#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Circle

import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(6,6))
plt.xlim(0,6)
plt.ylim(0,6)

theta = np.linspace(0, 2 * np.pi, 5)
center = [3,3]
radius = 2
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

print(f"theta = {np.round(theta,2)}")
print(f"x = {np.round(x,2)}")
print(f"y = {np.round(y,2)}")

plt.title('Circle - 5 points')
plt.plot(x, y,"bo-")
plt.show()


# In[55]:


plt.figure(figsize=(6,6))
plt.xlim(0,6)
plt.ylim(0,6)

theta = np.linspace(0, 2 * np.pi, 9)
center = [3,3]
radius = 2
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

print(f"theta = {np.round(theta,2)}")
print(f"x = {np.round(x,2)}")
print(f"y = {np.round(y,2)}")

plt.title('Circle - 9 points')
plt.plot(x, y,"bo-")
plt.show()


# In[56]:


plt.figure(figsize=(6,6))
plt.xlim(0,6)
plt.ylim(0,6)

theta = np.linspace(0, 2 * np.pi, 17)
center = [3,3]
radius = 2
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

print(f"theta = {np.round(theta,2)}")
print(f"x = {np.round(x,2)}")
print(f"y = {np.round(y,2)}")

plt.title('Circle - 17 points')
plt.plot(x, y,"bo-")
plt.show()


# In[57]:


plt.figure(figsize=(6,6))
plt.xlim(0,6)
plt.ylim(0,6)

theta = np.linspace(0, 2 * np.pi, 65)
center = [3,3]
radius = 2
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

print(f"theta = {np.round(theta,2)}")
print(f"x = {np.round(x,2)}")
print(f"y = {np.round(y,2)}")

plt.title('Circle - 65 points')
plt.plot(x, y,"bo-")
plt.show()


# In[58]:


# Perfect Heart Shape

import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(0, 2 * np.pi, 9)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 9 points')
plt.show()


# In[54]:


theta = np.linspace(0, 2 * np.pi, 21)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 21 points')
plt.show()


# In[59]:


theta = np.linspace(0, 2 * np.pi, 30)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"bo-")
plt.title('Heart Shape - 30 points')
plt.show()


# In[60]:


theta = np.linspace(0, 2 * np.pi, 100)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y,"b-")
plt.title('Heart Shape - 100 points')
plt.show()


# In[ ]:




