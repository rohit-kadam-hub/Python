
#topics
#Bubble sort / Insertion sort / Selection sort / Merge Sort / Quick sort / Heap Sort

##### BUBBLE SORT #############

def bubble(L):
    n=len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j]>L[j+1]:
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp
    return L

#Since no. of swappping in bubble sort is more ,consumes more power

### SELECTION SORT #####

def selection(L):

    for i in range(len(L)-1):
        minpos=i
        for j in range(i,len(L)):
            if L[j]<L[minpos]:
                minpos=j

        temp=L[i]
        L[i]=L[minpos]
        L[minpos]=temp
    return L

        
def insertion(L):
    for i in range(1,len(L)):
        temp=L[i]

        j=i-1
        while j>=0 and temp<L[j]:
            L[j+1]=L[j]
            j=j-1

        L[j+1]=temp
    return L
L=[2,5,3,3,3,8,4,2,1,7,9,5]
a=insertion(L)



def mergesort(List):
    if len(List)>1:
        mid=len(List)//2
        L=List[:mid]
        R=List[mid:]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                List[k]=L[i]
                i=i+1

            else:
                List[k]=R[j]
                j=j+1
            k=k+1

        while i<len(L):
            List[k]=L[i]
            i=i+1
            k=k+1

        while j<len(R):
            List[k]=R[j]
            j=j+1
            k=k+1

    return L

def partition(L,lb,ub):
    pivot=lb 
    start=lb
    end=ub
    while start<=end:
        while L[pivot]>=L[start] :
            start=start+1

        while L[pivot]<L[end]:
            end=end-1
            
        if start<=end:
            temp=L[start]
            L[start]=L[end]
            L[end]=temp
    
    temp=L[pivot]
    L[pivot]=L[end]
    L[end]=temp
    
    
    return end

def quicksort(L,lb,ub):
    print(lb,ub)
    print(L)
    if lb<ub:
        loc= partition(L,lb,ub)
        quicksort(L,lb,loc-1)
        quicksort(L,loc+1,ub)
        



L=[7,6]

print(partition(L,0,len(L)-1))





































    
