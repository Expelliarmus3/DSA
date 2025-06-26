'''Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4'''

# arr=[1, 2, 3, 4, 5]

# def getAlternates(arr):
#     myarr=[]
#     for i in range(0,len(arr),2):
#         myarr.append(i)
#     return myarr

# getAlternates(arr)

'''Input: arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
Output: 35
Explanation: The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 is common so we switch to arr1 and add 10 and 12.
'''

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
arr2 = [3, 4, 6, 7, 8]
# def maxPathSum(arr1, arr2):
    # Code here
path=[]
sum=0
max_in_1=0
min_in_2=0
path=[]
sum=0
max_in_1=0
min_in_2=0
if len(arr2)>len(arr1):
    for i,num in enumerate(arr1):
        if num in arr2:
            max_in_1=i
    for i,num in enumerate(arr2):
        if num in arr1:
            min_in_2=i
    for i in range(max_in_1):
        path.append(arr1[i])
    for i in range(min_in_2,len(arr2)):
        path.append(arr2[i])

    for items in path:
        sum+=items
        print(items)

else:
    for i,num in enumerate(arr2):
        if num in arr1:
            max_in_1=i
    for i,num in enumerate(arr1):
        if num in arr2:
            min_in_2=i
    for i in range(max_in_1):
        path.append(arr2[i])
    for i in range(min_in_2,len(arr1)):
        path.append(arr1[i])

    for items in path:
        sum+=items
        print(items)



print(sum)


    
    
    
                    
    