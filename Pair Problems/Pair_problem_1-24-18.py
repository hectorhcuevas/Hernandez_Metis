
# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[21]:

import numpy as np
candidate = np.arange(0.0, 10.0, 0.1)
candidate2 = np.arange(10.0,20.0,0.1)
numbers = np.array([2.0, 7.0, 1.0, 5.0, 10.0])


# In[23]:

candidate2


# def SLSE(numbers,ranges):
#     leastlist = []
#     best = 0
#     for number in candidate:
#        sqrs = 0
#        for item in numbers:
#            sqrs = (item - number)**2 + sqrs
#        leastlist.append(sqrs)
#        if sqrs == min(leastlist):
#            best = number
#     print(best)
#     plt.plot(leastlist)
# 

# In[24]:

SLSE(numbers, candidate2)


# In[ ]:



