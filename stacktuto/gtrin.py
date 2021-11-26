arr=[2,1,5,6,2,3]
n=len(arr)
def gtri(arr,n):
    s=[]
    r=[]
    for i in range(n-1,-1,-1):
        if len(s)==0:
            r.append(n)
        elif arr[i]<s[-1][0]:
            r.append(s[-1][1])
        elif arr[i]>=s[-1][0]:
            while(len(s)>0 and s[-1][0]<=arr[i]):
                s.pop()
            if len(s)==0:
                r.append(n)
            elif arr[i]<s[-1][0]:
                r.append(s[-1][1])
        s.append([arr[i],i])
    return r[::-1]
print(arr)
print(gtri(arr,n))