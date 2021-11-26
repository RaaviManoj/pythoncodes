s=input()

q=int(input())

def encode(s,q):
    arr=[]
    r=q%10
    for i in s:
        arr.append(ord(i)+r)
    
    for i in arr:
        arr[i]=arr[i]^q
    
    

def decode(s,q):
    pass