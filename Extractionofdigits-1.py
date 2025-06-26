import math

def get_fac_optimal_sol(n):
    factors=[]
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            factors.append(i)
            if n//i!=i:
                factors.append(n//i)
    factors.sort()
    return factors
def get_factor(n):
    factors=[]
    for i in range(1,(n//2)+1):
        if n%i==0:
            factors.append(i)
    factors.append(n)
    return factors
        
def chk_armstrong(n):
    sum=0
    count=count_digit_by_log(n)
    temp=n
    while n>0:
        sum+=(n%10)**count
        n=n//10
    n=temp
    return sum==n
def chk_palindrome(n):
    num= 0
    temp=n
    while n>0:
        num*=10
        num += n%10
        n=n//10
    n=temp
    return n==num

def rev_a_num(n):
    num= 0
    while n>0:
        num*=10
        num += n%10
        n=n//10        
    #num=num//10
    return num

def count_digit_by_log(n):
    return int(math.log10(n)+1)

def count_digits(n):
    count=0
    while n>0:
        digit=n%10
        count+=1
        n=n//10
    return count

def main():
    num =int(input("enter a num: "))
    # num_of_digits1=count_digits(num)
    # num_of_digits2= count_digit_by_log(num)
    # print(num_of_digits1)
    # print(num_of_digits2)
    # n= rev_a_num(num)
    # print(n)
    # is_palindrome=chk_palindrome(num)
    # print(is_palindrome)
    # p=chk_armstrong(num)
    # print(p)
    fac= get_fac_optimal_sol(num)
    print(fac)

if __name__=="__main__":
    main()