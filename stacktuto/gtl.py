arr=[6,5,8,4,7,10,9]
n=len(arr)
def gtl(arr,n):
    s=[]
    r=[]
    for i in range(n):
        if len(s)==0:
            r.append(-1)
        elif arr[i]<s[-1]:
            r.append(s[-1])
        elif arr[i]>=s[-1]:
            while(len(s)>0 and arr[i]>=s[-1]):
                s.pop()
            if len(s)==0:
                r.append(-1)
            elif arr[i]<s[-1]:
                r.append(s[-1])
        s.append(arr[i])
    return r
print(arr)
print(gtl(arr,n))