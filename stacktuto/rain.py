def rain(height):
    n=len(height)
    if n<=2:
        return 0
    a=[0]
    b=[]
    g=height[0]
    for i in range(n):
        if g>=height[i]:
            a.append(g)
        else:
            g=height[i]
            a.append(height[i])
    a.pop()

    g=height[-1]
    for i in range(n-1,-1,-1):
        if g>=height[i]:
            b.insert(0,g)
        else:
            g=height[i]
            b.insert(0,height[i])
    b.pop(0)
    b.append(0)
    #print(height)
    #print(a)
    #print(b)
    c=0
    for i in range(1,n-1):
        u=min(a[i],b[i])
        if u>height[i]:
            c+=u-height[i]
    return c
print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))