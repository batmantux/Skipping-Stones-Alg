#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import math
class SkippingStones:
    """ Class of SkippingStones """

    def __init__(self, o, M, a, N): # Variables
        self.o = o
        self.g = 9.8
        self.M = M
        self.d = 1000
        self.a = a
        self.C = 1
        self.N = N
        
       #Quatities required to optimise the initial velocity for a given no. of Skips on the water  
   
    def u(self): # Coeficient of friction equivalent 
        return (np.sin(np.radians(self.o)) + np.cos(np.radians(self.o))) / (np.cos(np.radians(self.o)) - np.sin(np.radians(self.o)))

    def L(self): # Length immersed in thee first skip 
        return 2*3.14*np.sqrt((2*(self.M)*np.sin(np.radians(self.o))/(self.C*self.d*self.a)))
   
    def Vc(self): # Critical velocity required for skipping
        return np.sqrt(2*(self.u())*(self.g)*(self.L()))
   
    def Vin(self): # input velocity given by the machine 
        return np.sqrt(((self.Vc())**2)*(self.N))

    def w(self): # angular velocity of the stone required for stabalization 
        return np.sqrt((self.N)*(self.g)/(self.a/2))
        
    def k(self): # extra condition
        return np.sqrt(2*(self.g)/(self.a)) 


# In[65]:


#for complete data set 
my_list=[]
for skips in np.arange(10,40,1):
    for mass in np.linspace(0,1,11):
        for length in np.linspace(0,1,11):
            for angle in np.arange(10,45,1):
                value = SkippingStones(o=angle, M=mass, a=length, N=skips)
                Velocity=value.Vin()
                Angular_Velocity= value.w()
                Coef = value.u()
                length_immersed = value.L()
                Critical_velocity = value.Vc()
           
                if 0<Velocity<10 and 0<Angular_Velocity<20: # limitations of the machine can be selected here 
                    z=[mass, length, angle, Coef, length_immersed,Critical_velocity, Velocity,Angular_Velocity,skips]
                    my_list.append(z)
my_list               
               
              


# In[66]:


# data for all combinations to give output No. of skips for a given input velocity 
import pandas as pd
df=pd.DataFrame(my_list, columns={'Mass':'0', 'Length':'1', 'Angle':'2','Coef':'3',' length_immersed':'4' ,'Critical_velocity':'5','Velocity':'6','Angular_Velocity':'7','skips':'8'})
df


# In[67]:


# To make subsets for analysis of varying parameter 
def return_subset(column, values, dataframe):
    df=dataframe.copy()
    return df[df[column].isin(values)]


# In[68]:


return_subset('Mass', [0.1], df) # set for constant mass of the stone.


# In[69]:


return_subset('Length', [0.5], df) # set for constant length of the stone.


# In[70]:


return_subset('Angle', [10], df) # set for constant angle of incidence with the water. 


# In[36]:


return_subset('Angular_Velocity', [10], df) # set for constant angular velocity of the stone.


# In[57]:


return_subset('skips', [10],df) # set for specific amounts of skips.


# In[64]:


df[(df.Mass.isin([0.1,1]))] # set for a specific  range of mass


# In[40]:


df[(df.Length.isin([0.1,1]))] # set for a specific range of length


# In[58]:


df[(df.Angle.isin([10,20]))] # set for a specific range of incidence angles 


# In[73]:


df[(df.Angular_Velocity.isin([11,12]))] # set for a specific range of angular velocity


# In[ ]:


df.to_csv(r'C:\Users\DELL\Desktop\Data_Set.csv', index=False)


# In[ ]:




