"""
def digit(num):
    value=0
    number=num
    while num!=0:
        rem=num%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        value=int(value+fact)
        num= int(num/10)
    print(value)
    if value==number:
        print("{} is a strong no.".format(number))
    else:
        print("{} is not a strong no.".format(number))
        
    
number=int(input("Enter a no. to check is it a strong or not :").strip())
digit(number)
"""
'''
#separate number or str
def separate(num):
    string=""
    while num!=0:
        rem=num%10
        
        string=string+str(rem)
        num=num//10
    string=str(string)
    return string
'''    
"""
#factorial
def factorial(num):
    if num==0:
        print("Fact of 0 is 1")
    
    elif num>0:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print("Fact of {} is {} ".format(num,fact))
    elif num<0:
        print("Invalid")

        
i=int(input())
factorial(i)
"""
"""
def perfect(num):
    number=num
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    
    if number==sum:
        print("{} is a perfect no".format(number))
    else:
        print("{} is not a perfect no".format(number))

i=int(input("Enter no :"))
perfect(i)
"""

"""
#perfect pair
def pair(num1,num2):
    sum1=0
    sum2=0
    number1=num1
    number2=num2
    sum=0
    for i in range(1,num1):
        if num1%i==0:
            sum1=sum1+i
    print(sum1)
    for i in range(1,num2):
        if num2%i==0:
            sum2=sum2+i
    print(sum2)
    
    if sum1==number1 and sum2==number2:
        print("{} and {} are pair  no".format(number1,number2))
    else:
        print("{} and {} are not pair no".format(number1,number2))

number1=int(input("Enter no n1 :"))
number2=int(input("Enter no n2 :"))
pair(number1,number2)


"""
"""
#Automorphic 5*5=25 , 6*6=36 , last no. is same as no. itself

def automorphic(num):
    number=num
    print(num)
    square=num*num
    print(square)
    rem=0
    s=separate(square)
    
    if int(s[0])==number:
        print("it is a automorphic")
    else:
        print("Its not a automorphic ")
    
    
    
i=int(input("Enter a no :").strip())
automorphic(i)
    
"""

"""
def factors(num):
    count=0
    print("The factors of",num,"are",end=" ")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            count=count+1
    print("total: ",count)
        

factors(60)

"""
"""
def prime(a,b):
    
    while a<b:
        flag=0
       
        for i in range(2,int(a),1):
            if a%i==0:
                flag=1
                break
                
        if flag ==0:
            print(a)
        a=a+1
    
prime(1,50)
"""

"""
# Python program to print the Armstrong numbers between the two intervals

import math
start = int(input("Enter start value : "))
end = int(input("Enter end value : "))
result = 0
n = 0
for i in range(start+1 ,end,1):
    temp2 = i
    temp1 = i

    while (temp1 != 0):
        temp1 = int(temp1/10)
        n = n + 1
        

    while (temp2 != 0):
        remainder = temp2 % 10
        result = result + math.pow(remainder, n)
        temp2 = int(temp2/10)

    if (result == i):
        print(i," ")

    n = 0
    result = 0

"""

"""

def arm(a,b):
    res=0
    for i in range (a,b):
        temp1=i
        n=len(str(temp1))
        while temp1!=0:
            rem=temp1%10
            res=res+rem**n
            temp1=temp1//10
        if res==i:
            print(i)
        n=0
        res=0

arm(100,500)
"""

"""
def prime_two(a,b):
    
    while a<=(b//2):
        flag=0
        for i in range(2,int(a/2),1):
            if a%i==0:
                flag=1
                break
        if flag==0:
            temp=prime(b-a)
            if temp==True:
                print("{}+{}={}".format(b-a,a,b))
        a=a+1

def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag==1
            return False
        
    if flag==0:
        return True

a=prime(3)
print(a)
prime_two(0,34)    
"""
"""
#same for practice
def prime(num):
    flag=0
    for i in range(2,num//2):
        
        if num%i==0:
            flag=1
            
            return False
            break
    if flag==0:
        return True

def pmt(a,b):
    while a<=b//2:
        flag=0
        for i in range(2,a//2):
            if a%i==0:
                flag=1
                break
        if flag==0:
            temp=prime(b-a)
            if temp==True:
                print("{}={}+{}".format(b,a,b-a))
            
        a=a+1

x=int(input())
pmt(0,x)
"""

"""
def zero_to_one(num):
    st=""
    while num!=0:
        rem=num%10
        if rem==0:
            rem=1

        st=str(rem)+st
        num=num//10
    print(st)    
zero_to_one(56004)
"""

"""
import math
def bin_to_dec(binary):
    n=0
    num=binary
    print(binary)
    while binary!=0:
        binary=binary//10
        n=n+1
    
    
    res=0
    for i in range(0,n):
        rem=num%10
        res=res+rem*(2**i)
        num=num//10
    print(res)
        
    
bin_to_dec(1100)
"""







        
        




             
