ti=[1,3,5,8,9,2,6,7,6,8,9]
n=len(ti)

def mjum(m,n):
    if m==n:
        return 0
    if ti[m]==0:
        return float('inf')
    j=ti[m]
    mi=float('inf')
    for i in range(m+1,n+1):
        if i<m+j+1:
            po=mjum(i,n)
            if (po!=float('inf')) and (po+1<mi):
                mi=po+1
    return mi
print(mjum(0,n-1))
