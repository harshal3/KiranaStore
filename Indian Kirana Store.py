#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum=0
while(True):
    userinput=(input("enter the price"))
    if(userinput!='q'):
        sum=sum + int(userinput)
        print("your total so far is",sum)
    else:
        print("Your bill total is",sum)
        print("thanks for shopping with us...")
        break 
        
    
    


# In[ ]:




