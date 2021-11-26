class arrstack:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*self.size
        self.lsize=0
        self.rsize=0
        self.ltop=-1
        self.rtop=self.size

    def ltopval(self):
        return self.arr[self.ltop]
    def rtopval(self):
        return self.arr[self.rtop]

    def push(self,side,val):
        if self.size-self.lsize-self.rsize==0:
                print("stack OverFlow")
                return
        if side=="l": 
            self.ltop+=1
            self.arr[self.ltop]=val
            self.lsize+=1
        else:
            self.rtop-=1
            self.arr[self.rtop]=val
            self.rsize+=1
    def pop(self,side):
        if side=="l":
            if self.ltop==-1:
                print("stack UnderFlow")
                return 
            self.arr[self.ltop]=-1
            self.ltop-=1
            self.lsize-=1
        else:
            if self.rtop==self.size:
                print("stack UnderFlow")
                return 
            self.arr[self.rtop]=-1
            self.rtop+=1
            self.rsize-=1
    def sprint(self):
        print(self.arr)
st=arrstack(5)


st.push("l",5)
st.push("l",11)
st.push("r",10)
st.push("r",15)
st.push("r",7)
st.sprint()
print(st.rtopval())
print(st.ltopval())
st.sprint()