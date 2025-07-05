count=0
def fact(N):
    if N==0 or N==1:
        return 1
    return N*fact(N-1)
def rec():
    global count 
    if count==4:
        return 0
    else:
        print("hi")
        count+=1
        rec()

def rec_with_par(x,n):
    if n==0:
        return 0
    else:
        print(x)
        rec_with_par(x,n-1)

def rec1(N):
    if N==0:
        return 0
    rec1(N-1)
    print(N)

def rec2(i,N):
    if i>N:
        return 0 
    else:
        print(i)
        rec2(i+1,N)
    

# rec_with_par('Meow',4)
# rec()
# rec1(6)
# rec2(1,6)
num= int(input("Enter a number to get its factorial: "))
x= fact(num)
print(x)