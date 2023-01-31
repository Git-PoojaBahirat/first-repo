#!/usr/bin/env python
# coding: utf-8

# In[1]:


Balance=65300
psw=int(input("enter your pin: "))
if psw==1523:
    print("welcome")

    #while psw==1532:
    a=int(input("choose any of the following:\n 1:balance enquiry:\n 2:withdrawl\n 3:exit"))
    if(a==1):
             print("The available balance is: ",Balance )
    elif(a==2):
            b = int(input("Enter amount of money:"))
            if(b<=Balance):
                    print("take your cash")
                    Balance=Balance-1
               
            else:
                    print("entered amount is not available in your account")
                    
    elif(a==3):
             print("exit")
    
else:
    print("pin is invalid \n")
    print("please enter valid pin")
    
      


# In[ ]:



      

