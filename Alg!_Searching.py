
#Linear Search
#Time complexity = O(n)

"""
x=int(input("Searchiing Element : "))
L=[10,20,30,40,50,110,100,130,140]

def searching(List,element):
    print(List)
    n=len(L)
    flag=0
    i=0
     
    for i in range(n-1):   
        if List[i]==element:
            print("{} is at {}".format(element,i))
            flag=1
        i=i+1
    if flag==0:
        print("Element you entered does not exists in given list")

searching(L,x)

"""
#Binary Search
#TIME COMPLEXITY : O(log n)
"""
def bin_search(L,base,n,x):

    if n>=base:
        mid=base+(n-base)//2

        if mid==x:
            return mid
        elif mid<x:
            return bin_search(L,mid+1,n,x)
        else:
            return bin_search(L,base,mid-1,x)

    else:
        return -1
    

L=[1,2,3,4,5]
x=5
r=bin_search(L,0,len(L),x)

print(r)
 
"""
"""
def BinarySearch(List,start,end,element):

    if end>=start:
        mid= start+(end-start)//2

        if List[mid]==element:
            return mid
        elif List[mid]<element:
            return BinarySearch(List,mid+1,end,element)
        else:
            return BinarySearch(List,start,mid-1,element)
    else:
        return -1
        
L=[1,2,3,4,5,6,7,8,9,10,11]
x=10
result=BinarySearch(L,0,len(L)-1,x)
if result == -1:
    print("The element not found")

else:
    print("The element is at",result,"position")
    
"""
"""
# Python program to implement interpolation search 

# If x is present in arr[0..n-1], then returns 
# index of it, else returns -1 
def interpolationSearch(arr, n, x): 
	# Find indexs of two corners 
	lo = 0
	hi = (n - 1) 

	# Since array is sorted, an element present 
	# in array must be in range defined by corner 
	while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
		if lo == hi: 
			if arr[lo] == x: 
				return lo; 
			return -1; 
		
		# Probing the position with keeping 
		# uniform distribution in mind. 
		pos = lo + int(((float(hi - lo) /
			( arr[hi] - arr[lo])) * ( x - arr[lo]))) 

		# Condition of target found 
		if arr[pos] == x: 
			return pos 

		# If x is larger, x is in upper part 
		if arr[pos] < x: 
			lo = pos + 1; 

		# If x is smaller, x is in lower part 
		else: 
			hi = pos - 1; 
	
	return -1

# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, \ 
				22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 

x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 

if index != -1: 
	print "Element found at index",index 
else: 
	print "Element not found"

# This code is contributed by Harshit Agrawal 
"""

"""

def interpolationSearch(List,n,x):
    lo=0
    hi= (n-1)
    print(List)

    while lo<=hi and x>=List[lo] and x<=List[hi]:
        if lo==hi:
            if List[lo]==x:
                return lo
            return -1

         
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo])))
        
        if List[pos] ==x:
            return pos
        elif List[pos]<x:
            lo=pos+1

        else:
            hi=pos-1

    return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 

x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 

if index != -1:
	print ("Element found at index",index )
else: 
	print ("Element not found")

"""
"""
def fibonacciGenerator(n):
   
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacciGenerator(n-1)+fibonacciGenerator(n-2)


def FiboSearch(arr,x):

    m=0
    while fibonacciGenerator(m)<len(arr):
        m=m+1


    offset=-1

    while fibonacciGenerator(m)>1:

        i= min(offset+fibonacciGenerator(m-2), len(arr)-1)

        if x>arr[i]:
            m=m-1
            offset=i

        elif x<arr[i]:
            m=m-2

        else:
            return i


    if fibonacciGenerator(m-1) and arr [offset+1]==x:
        return offset+1


    return -1
arr=[10,20,30,40,50,60,70,80,90,100,110,120,130]
x=200
print(FiboSearch(arr,x))


#Fibo again

def fibogen(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return fibogen(n-2)+fibogen(n-1)

def fibosearch(arr,x):
    m=0
    while fibogen(m)<len(arr)-1:
        m=m+1
    
    offset=-1
    while fibogen(m)>1:
    
        i=min(offset+fibogen(m-2),len(arr)-1)

        if x>arr[i]:
            m=m-1
            offset=i

        elif x<arr[i]:
            m=m-2

        else:
            return i

    if fibogen(m-1) and arr[offset+1]==x:
        return offset+1

    return -1

        
arr=[1,2,3,4,5,6,7,8,9]
x=7
print(fibosearch(arr,x))

"""

# 0 1 1 2 3 5 8 13 
def fibgen(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return fibgen(n-1)+fibgen(n-2)


def fibsearch(arr,x):
    m=0
    while fibgen(m)<len(arr):
        m=m+1
    print(m)
    offset=-1
    while fibgen(m)>1:

        i=min(offset+fibgen(m-2),len(arr)-1)

        if arr[i]<x:
            m=m-1
            offset=i

        elif arr[i]>x:
            m=m-2

        else:
            return i

    if fibgen(m-1) and arr[offset+1]==x:
        return offset+1
    
    return -1

arr=[1,2,3,4,5]
x=5
print(fibsearch(arr,x))



























    






















      
