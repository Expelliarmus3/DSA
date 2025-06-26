# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]
# hash_list={}
# for i in range(0,len(n)):
#     if n[i] in n:
#         hash_list[n[i]]=hash_list.get(n[i],0)+1
#     else:
#         hash_list[n[i]]=hash_list.get(n[i],0)

# for num in m:
#     if num in hash_list:
#         print(hash_list[num])
#     else:
#         print(0)

s="azyxyyzaaaa"
q=["d","a","y","x"]
hash={}
for ch in q:
    count=0
    for x in s:
        if x== ch:
            count+=1
    print(count)