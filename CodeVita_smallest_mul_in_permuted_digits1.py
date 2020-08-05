def separate(n):
    L=[]
    while n!=0:
        rem= n%10
        L.append(rem)
        n=n//10
    reverse(L)
    sort(L)
    return L

def reverse(L):
    for i in range(0,len(L)//2):
        temp=L[i]
        L[i]=L[-(i+1)]
        L[-(i+1)]=temp
        
    return L

def sort(L):
    for i in range(0,len(L)-1):
        for j in range(len(L)-1):
            if L[j]>L[j+1]:
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp

    return L
# Python function to print permutations of a given list 


def  permutation(string,start,end):
    current=0
    if start==end-1:
        if not string in result:
            result.append(string)

    else:
        for current in range(start,end):
            x=list(string)
            temp=x[start]
            x[start]=x[current]
            x[current]=temp
            permutation("".join(x),start+1,end)
            temp=x[start]
            x[start]=x[current]
            x[current]=temp
            

def main(N,d):
    L=separate(N)
    print(L)
    for i in range(len(L)):
        L[i]=str(L[i])
    L="".join(L)
    permutation(L,0,len(L))
    L=list(result)
    return L
            
if __name__=="__main__":
    N=int(input("Input digit: ").strip())
    d=int(input("d: ").strip())
    result=list()
    L=main(N,d)
    print(L)
    flag=0
    for j in range(len(L)):
        if int(L[j])%d==0:
            print(L[j])
            flag=1
            break

    if flag==0:
        print("-1")
    
    











    









    
    

