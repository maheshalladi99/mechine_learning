import numpy as np
import random
print("\n         WELCOME TO SNAKES AND LADDERS GAME \n")
a=int(input("HOW MANY PLAYES WANT TO PLAY?(MAX PLAYESRS 3)"))
for i in range(1,a+1):
    print("{} player names is Player{}".format(i,i))
l=[]
i=1
for k in range(0,10):
    l1=[]    
    while(True):
        l1.append(i)
        if (i%10==0):
            i+=1
            break
        i+=1
    l.append(l1)
#l=np.array(l)
l.reverse()
#print(l)
#def mov(l,p):
    
l2=[18,36,55,78,92,25,28,46,69,85]
##while(True):
##    d=random.randint(1,100)
##    if d not in l2: 
##        l2.append(d)
##    if len(l2)==10:
##        break
#print(l2)
for k in range(0,5):
    for j in range(0,10): 
        if l2[k] in l[j]:
            m=l[j].index(l2[k])
            l[j][m]=9999
for k in range(5,10):
    for j in range(0,10): 
        if l2[k] in l[j]:
            m=l[j].index(l2[k])
            l[j][m]=1111    
#print(l)
#l=np.array(l)
print("\n         WELCOME TO SNAKES AND LADDERS GAME \n")

print(np.array(l))
print("\n9999 means snake, 1111 means ladder")
d=1
while True:
    for i in range(1,a+1):
        print("player ",i," Turn,press enter")
        z=input()
        p=random.randint(1,6)
        print("player",i,"got:",p)
        print("\n \n",np.array(l))
        #mov(l,p)
        
        
    
