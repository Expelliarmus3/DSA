#Reverse an array using recursion

# def rev(arr,left,right):
    
#     if left>=right:
#         print(arr)
#         return 
#     temp=arr[left]
#     arr[left]=arr[right]
#     arr[right]=temp
#     rev(arr,left+1,right-1)



# rev(l,2,5)
l=[5,7,3,2,6,1,5,9]
def func(arr,left,right):
    if left>=right:
        return 
    arr[left],arr[right]=arr[right],arr[left]
    return func(arr,left+1,right-1)
func(l,0,7)
print(l)


# left,right=0,len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1

# print(l)