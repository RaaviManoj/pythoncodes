s=[]
mi=0
def push(n):
    global mi
    if len(s)==0:
        s.append(n)
        mi=n
    elif n<mi:
        u=(2*n)-mi
        s.append(u)
        mi=n
    else:
        s.append(n)

def pop():
    global mi
    if len(s)==0:
        return -1
    elif s[-1]<mi:
        mi=(2*mi)-s[-1]
        s.pop()
    else:
        s.pop()

def top():
    if len(s)==0:
        return -1
    elif s[-1]<mi:
        return mi
    else:
        return s[-1]
    
def mini():
    return mi

push(5)
print(s)
print(mini())
print(top())
push(3)
print(s)
print(mini())
print(top())
push(1)
print(s)
print(mini())
print(top())
pop()
print(s)
print(mini())
print(top())