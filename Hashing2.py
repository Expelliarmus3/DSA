'''constraints: 1<=n<=10
n and m has 10^8 elements'''
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list= [0]*11
for num in n:
    hash_list[num]+=1
#print(hash_list)
for num in m:
    if num>10 or num<1:
        print(0)
    else:
        print(hash_list[num])