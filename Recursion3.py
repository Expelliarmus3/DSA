#Palindrome of strings

import random
#via loop

s=['nitin','mom','Maze','pea','rotor','kayak']
str= random.choice(s)


def chk_pal(s):
    l=0
    r=len(s)-1
    flag=0
    while l<r:
        if s[l].lower()==s[r].lower():
            flag=1
            l+=1
            r-=1
        else:
            flag=0
            break
    if flag==1:
        return True
    else:
        return False
    
# val=chk_pal(str)
# print(val,str)

# via recursion

def pal(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return pal(s,l+1,r-1)
    
# word="sts"
# val= pal(word,0,len(word)-1)
# print(val)

#FIBONACCI NUMBER

def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)

n=9
num=fibo(n) 
print(num)

        

        