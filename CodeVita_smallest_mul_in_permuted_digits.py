"""
Question:
Smallest Multiple in permuted digits

"""

"""
def split(num):
    L=[]
    while num != 0:
        rem=num%10
        L.append(rem)
        num=num//10
    list.reverse(L)
    list.sort(L)
    print(L)


def sort

N=int(input().strip())
split(N)
d=int(input().strip())

"""
#Array Rotation
"""
def arr_rot_by_one(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def arr_rot(arr,d,n):
    for i in range(d):
        arr_rot_by_one(arr,n)

def printArray(arr, size): 
    for i in range(size): 
        print ("",arr[i], end =" ")

arr=[1,2,3,4,5]
a=arr_rot(arr,2,5)
printArray(arr,5)

"""
# Array rotetion
""" 
def array_rotation(arr,n,d):
    for i in range(d):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp

arr=[1,2,3,4,5,6,7]
array_rotation(arr,7,2)
print(arr)

"""
#reverse algorithm
"""
def reverse(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1


def left(arr,d):
    if d==0:
        return
    n=len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

def right(arr,d):
    if d==0:
        return
    n=len(arr)
    reverse(arr,n-d,n-1)
    reverse(arr,0,n-d-1)
    reverse(arr,0,n-1)

def list_(n):
    L=[]
    while n!=0:
        i=int(input("input the list number"))
        L.append(i)
        n=n-1
    return L


l=int(input("Length of array : "))
arr=list_(l)
d=1
print("Left shift of arr",arr ,"by",d,"is" ,end= " ")
left(arr,d)
print(arr)


l=int(input("Length of array : "))
arr=list_(l)
d=1
print("Right shift of arr",arr ,"by",d,"is" ,end=" ")
right(arr,d)
print(arr)
"""

#Product of subarrays

def product_sub(arr,n):
    product=1
    for i in range(0,n):
        L=[]
        pd=1
        for j in range(i,n):
            L.append(arr[j])
            pd=pd*arr[j]
            
            if len(L)==2:
                print(L)    
        product=product*pd
    # Printing product of all subarray 
    print(product, "\n"); 
  
# Driver code 
arr = [28,12,40,76,40,76,40,11,19,18]; 
  
n = len(arr); 
  
# Function call 
product_sub(arr, n);





















































    
