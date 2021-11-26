arr=[2,1,5,6,2,3]
n=len(arr)

def stolein(arr,n):
    s=[]
    r=[]
    for i in range(n):
        if len(s)==0:
            r.append(-1)
        elif arr[i]>s[-1][0]:
            r.append(s[-1][1])
        elif arr[i]<=s[-1][0]:
            while(len(s)>0 and arr[i]<=s[-1][0]):
                s.pop()
            if len(s)==0:
                r.append(-1)
            elif arr[i]>s[-1][0]:
                r.append(s[-1][1])
        s.append([arr[i],i])
    return r


def storin(arr,n):
    s=[]
    r=[]
    for i in range(n-1,-1,-1):
        if len(s)==0:
            r.append(n)
        elif arr[i]>s[-1][0]:
            r.append(s[-1][1])
        elif arr[i]<=s[-1][0]:
            while(len(s)>0 and arr[i]<=s[-1][0]):
                s.pop()
            if len(s)==0:
                r.append(n)
            elif arr[i]>s[-1][0]:
                r.append(s[-1][1])
        s.append([arr[i],i])
    return r[::-1]


def holo(arr,n):
    c=0
    x=stolein(arr,n)
    y=storin(arr,n)
    for i in range(n):
        z=(y[i]-x[i]-1)*arr[i]
        if z>c:
            c=z
    return c
print(holo(arr,n))

