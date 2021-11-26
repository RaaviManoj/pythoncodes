class node:
        def __init__ (self,data):
            self.data=data
            self.prev=None
            self.next=None

class doublelinked:
    def __init__(self):
        self.head=None
        self.tail=None   
        self.size=0

    def add(self,node):
        self.size+=1
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=node
            node.prev=temp
            self.tail=node
    
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def printrev(self):
        temp=self.tail
        while(temp):
            print(temp.data,end=" ")
            temp=temp.prev
        print()

    def insert(self,node,pos):
        if pos==0:
            self.size+=1
            node.next=self.head
            self.head.prev=node
            self.head=node
        elif pos==self.size:
            return self.add(node)
        else:
            self.size+=1
            temp=self.head
            c=0
            while(temp):
                if c==pos-1:
                    tp=temp.next
                    temp.next=node
                    node.prev=temp
                    node.next=tp
                    tp.prev=node
                c+=1
                temp=temp.next
    
    def remove(self,pos):
        if pos==0:
            self.size-=1
            self.head=self.head.next
            self.prev=None
        elif pos==self.size-1:
            return self.pop()
        else:
            self.size-=1
            temp=self.head
            c=0
            while(temp.next):
                if c==pos-1:
                    temp.next=temp.next.next
                    temp.next.prev=temp
                else:
                    temp=temp.next
                c+=1

    def delete(self,val):
        flag=True
        if self.head.data==val:
            self.size-=1
            self.head=self.head.next
            self.head.prev=None
        else:
            temp=self.head
            while(temp.next.next):
                if temp.next.data==val:
                    self.size-=1
                    temp.next=temp.next.next
                    temp.next.prev=temp
                    flag=False
                    break
                else:
                    temp=temp.next
        if flag:
            if self.tail.data==val:
                return self.pop()
    """
    def removeall(self,val):
        if self.head.data==val:

            self.head=self.head.next
        else:
            temp=self.head
            while(temp.next and temp.next.next):
                if temp.next.data==val:
                    self.size-=1
                    temp.next=temp.next.next
                    temp.next.prev=temp
                else:
                    temp=temp.next
    """

    def pop(self):
        self.size-=1
        self.tail=self.tail.prev
        self.tail.next=None

    def reverse(self):
        temp=self.tail
        while(temp):
            tp=temp.next 
            temp.next=temp.prev
            temp.prev=tp
            temp=temp.next
        tmp=self.head
        self.head=self.tail
        self.tail=tmp





            

dl=doublelinked()
dl.add(node(10))
dl.add(node(15))
dl.add(node(3))
dl.insert(node(60),0)

dl.add(node(15))
dl.add(node(15))
dl.add(node(15))

dl.insert(node(0),3)
dl.print()
print(dl.size)
#dl.printrev()
dl.remove(15)
dl.print()
dl.printrev()


        