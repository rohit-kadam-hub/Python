"""
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None :
            print("the list is empty")
            return

        itr=self.head
        llstr=""
        while itr:
            llstr += str(itr.data)+"-->"
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr =self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begin(5)
    ll.insert_at_begin(6)
    ll.insert_at_begin(5)
    ll.insert_at_begin(5)
    ll.insert_at_end(10)
    ll.print()
"""
class Node:
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr=llstr+str(itr.data)+"-->"
            itr=itr.Next
            
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.Next:
            itr=itr.Next
        itr.Next=Node(data,None)

ll=LinkedList()
ll.insert_at_begin(5)
ll.print()
ll.insert_at_begin(7)
ll.print()
ll.insert_at_end(5)
ll.print()




































    
