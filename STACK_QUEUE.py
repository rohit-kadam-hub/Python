"""

def push(L,N,top):
    data=int(input("Enter the data : ").strip())

    if top==N-1 :
        print("Overflow")

    else:
        top=top+1
        
        L.append(data)

    

def pop(L,N,top):
    if top == -1:
        print("Underflow")

    else:
        L.remove(top)
            top=top-1
        
def display(L,N,top):
    for i in range(len(L)):
        print(L[i])



def top(L,N,top):
    if top==-1:
        print("Stack is empty")

    else:
        print(top)

top=-1
N=5
stack=[1,2,3]
push(stack,N,top)
print(top,N,stack)
push(stack,N,top)
print(top,N,stack)
push(stack,N,top)
print(top,N,stack)
"""
"""
stack=[]
stack.append("a")
stack.append("b")
stack.append("c")

print("Initial Stack: ",stack)

stack.pop()
print(stack)
stack.append("a")
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

"""
# Stack collection , deque TC=O(1)
"""
from collections import deque
class stack :
    def __init__(self):
        self.container=deque()
        
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
            
    def display(self):
        return self.container

    def top(self):
        
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

def reverse_string(s):
    Stack = stack()

    for ch in s:
        Stack.push(ch)

    rstr = ''
    
    while Stack.size() !=0:
        rstr += Stack.pop()

    return rstr

def is_match(ch1,ch2):
    match_dict={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    return match_dict[ch1]==ch2

def is_balanced(s):
    Stack=stack()
    for ch in s:
        if ch=="(" or ch =="{" or ch=="[":
            Stack.push(ch)
        if ch==")" or ch=="}"or ch=="]":
            if Stack.size()==0:
                return False
            if not is_match (ch,Stack.pop()):
                return False
    return Stack.size()==0

if __name__== "__main__":
    print(is_balanced("({a+b})"))
"""    
    
#Queue collection
import time
import threading


from collections import deque
class queue :
    def __init__(self):
        self.container=deque()
        
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
            
    def display(self):
        return self.container

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
    def front(self):
        return self.container[-1]


def produce_binary(n):
    no=queue()
    no.enqueue("1")
    for i in range(n):
        front=no.front()
        print(" ",front)
        no.enqueue(front+"0")
        no.enqueue(front+"1")
        no.dequeue()
        
food_order_queue=queue()    
def place(orders):
    for order in orders:
        print("Place order for :",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        order=food_order_queue.dequeue()
        print("now serving : ",order)
        time.sleep(2)

if __name__=="__main__":
    orders=["pizza","samosa","pasta","biryani","burger"]
    t1=threading.Thread(target=place, args=(orders,))
    t2=threading.Thread(target=serve_order)

    t1.start()
    t2.start()




















    
