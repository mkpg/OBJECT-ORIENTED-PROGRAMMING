#!/usr/bin/env python
# coding: utf-8

# In[118]:


class Account:
    def __init__(self,owner,balence):
        self.owner=owner
        self.balence=balence
    def __str__(self):
        return f"Account owner:{self.owner}\nAccount balence:${self.balence}"
        
    def deposit(self,amt):
        self.balence+=amt
        print("Deposit Accepted")
        
        
    def Withdraw(self,withdraw):
        if self.balence >= withdraw:
            self.balence-=withdraw
            print("Withdrawal Accepted")
        else:
            print("Funds insuffecient")
        


# In[119]:


account = Account('Jose',100)


# In[120]:


print(account)


# In[121]:


account.owner


# In[127]:


account.balence


# In[128]:


account.deposit(500)


# In[129]:


account.Withdraw(800)


# In[130]:


account.Withdraw(500)


# In[ ]:





# In[ ]:




