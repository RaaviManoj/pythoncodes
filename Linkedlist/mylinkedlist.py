class node:
    def __init__(self,val):
        self.next=None
        self.val=val

class linked:
    def __init__(self):
        self.head=None
        self.size=0

    def print(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
        print()
    
    def add(self,node):
        self.size+=1
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=node

    def insert(self,pos,node):
        self.size+=1
        if pos==0:
            node.next=self.head
            self.head=node
        else:
            temp=self.head
            c=0
            while(temp):
                if c==pos-1:
                    pq=temp.next
                    temp.next=node
                    node.next=pq
                c+=1
                temp=temp.next
    
    def remove(self,pos):
        if pos==0:
            self.head=self.head.next
        else:
            temp=self.head
            c=0
            while(temp and temp.next):
                if c==pos-1:
                    temp.next=temp.next.next
                else:
                    temp=temp.next
                c+=1

    def removeall(self,val):
        while self.head.val==val:
            self.head=self.head.next
        temp=self.head
        while(temp and temp.next):
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        
    def removeone(self,val):
        if self.head.val==val:
            self.head=self.head.next
        else:
            temp=self.head
            while(temp and temp.next):
                if temp.next.val==val:
                    temp.next=temp.next.next
                else:
                    temp=temp.next
                break


    def reverse(self):
        if self.size==0:
            return 
        temp=self.head
        pre=None
        ne=None
        while(temp):
            ne=temp.next
            temp.next=pre
            pre=temp
            temp=ne
        self.head=pre


def intersecofsorted(head1,head2):
    t1=head1;t2=head2
    dum=node(0)
    tail=dum
    while(1):
        if not t1:
            tail.next=t2
            break
        if not t2:
            tail.next=t1
            break

        if t1.val<=t2.val:
            tail.next=t1
            t1=t1.next
        else:
            tail.next=t2
            t2=t2.next
        tail=tail.next
    return dum.next

if __name__=="__main__":
    arr1=[0,2,2,3,4,6]
    arr2=[1,2,6,8]
    p=linked()
    q=linked()
    for i in arr1:
        p.add(node(i))
    for i in arr2:
        q.add(node(i))
    intersecofsorted(p.head,q.head)
    if p.head.val<=q.head.val:
        p.print()
    else:
        q.print()
    




