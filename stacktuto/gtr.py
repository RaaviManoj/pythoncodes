def gtr(arr,n):
    s=[]
    r=[]
    for i in range(n-1,-1,-1):
        if len(s)==0:
            r.append(-1)
        elif arr[i]<s[-1]:
            r.append(s[-1])
        elif arr[i]>=s[-1]:
            while(len(s)>0 and s[-1]<=arr[i]):
                s.pop()
            if len(s)==0:
                r.append(-1)
            elif arr[i]<s[-1]:
                r.append(s[-1])
        s.append(arr[i])
    return r[::-1]

def grater_to_right(arr,n):
    res=[];stack=[]
    for i in range(n-1,-1,-1):
        if not stack: res.append(-1)
        elif arr[i]<stack[-1]: res.append(stack[-1])
        elif arr[i]>=stack[-1]:
            while stack and arr[i]>=stack[-1]:
                stack.pop()
            if not stack: res.append(-1)
            elif arr[i]<stack[-1]: res.append(stack[-1])
        stack.append(arr[i])
    return res[::-1]

if __name__=="__main__":
    
    arr=[6,7,4,3,5,2]
    n=len(arr)
    print(gtr(arr,n))
    print(grater_to_right(arr,n))