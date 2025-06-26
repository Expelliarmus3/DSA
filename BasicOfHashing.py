
def freq_map(num,x):
    map={}
    for i in range(0,len(num)):
        if num[i] in map:
            map[num[i]]+=1
        else:
            map[num[i]]=1
    if x in map:
        print(map[x])
    else:
        print("Doesnt exist")


def main():
    num=[1,1,2,4,5,5,3,4]
    n= int(input("Enter the number whose freq you wanna know: "))
    freq_map(num,n)
main()