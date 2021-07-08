#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
a=np.arange(40,50)
b=np.arange(50,60)
x_values = [a[0], b[0]]
y_values = [a[1], b[1]]
plt.plot(x_values, y_values)


# In[20]:


import matplotlib.pyplot as plt
sales_1 = [160,150,140,145,175,165,180] 
sales_2 = [70,90,160,150,140,145,175]  
line_chart1 = plt.plot(range(1,6), sales1,'--')
line_chart2 = plt.plot(range(1,6), sales2,':')
plt.title('Daily sales of Salesman1 and Salesman2')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.legend(['Sales of salesman 1', 'Sales of salesman 2'], loc=4)
plt.show()


# In[26]:


import matplotlib.pyplot as plt
 
x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

fig, ax = plt.subplots(3)
fig, ax1=plt.subplots(2)
 
ax[0].plot(x, y1)
ax[1].plot(x, y2)
ax[2].plot(x, y3)

ax1[0].plot(x, y4)
ax1[1].plot(x, y5)

