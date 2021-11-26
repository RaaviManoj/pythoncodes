#most optimal solution
ld=[0]*30
rd=[0]*30
column=[0]*30
res=[]

def store(grid):
    tem=[]
    for i in grid: tem.append(" ".join(i))
    res.append(tem)

def opt_nqueen(col,ans,n):
    if col>=n: return True
    for i in range(n):
        if ld[i-col+n-1]!=1 and rd[i+col]!=1 and column[i]!=1:
            ans[i][col]='Q'; ld[i-col+n-1]=1; rd[i+col]=1; column[i]=1
            if opt_nqueen(col+1,ans,n):
                store(grid)
            ans[i][col]='.'; ld[i-col+n-1]=0; rd[i+col]=0; column[i]=0
    #print(column)
    return False




if __name__=="__main__":
    n=4
    grid=[['.']*n for i in range(n)]
    #print(grid)
    opt_nqueen(0,grid,n)
    print(res)