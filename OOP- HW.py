#!/usr/bin/env python
# coding: utf-8

# In[32]:


import cmath
class Line:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def distance(self):
        print(cmath.sqrt((self.c-self.a)**2+(self.d-self.b)**2))
    def slope(self):
        print((self.d-self.b)/(self.c-self.a))


# In[33]:


line = Line(a=3,b=2,c=8,d=10)


# In[34]:


line.distance()


# In[35]:


line.slope()


# In[ ]:




