
# coding: utf-8

# In[4]:


import numpy as np
import math


# In[21]:


class node:
    def __init__(self,args):
        self.w1 = np.random.randn(args[1],args[0])
        self.w2 = np.random.randn(args[2],args[1])
        self.b1 = np.random.randn(args[1],1)
        self.b2 = np.random.randn(args[2],1)
    def disp(self):
        print(self.w1,self.w2)
    def sigmoid(self,arr):
        self.z = arr
        for i in range(arr.len):
            arr[i] = 1/(1+math.exp(-arr[i]))


# In[20]:


n = node([10,5,3])

