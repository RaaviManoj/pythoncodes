import time
#it'snot the optimal solution
def is_safe(i,j,n,ans):
    row=[0,1,1,1,0,-1,-1,-1]; col=[-1,-1,0,1,1,1,0,-1]
    for z in range(8):
        x=i;y=j
        while x<n and x>=0 and y>=0 and y<n:
            if ans[x][y]==1: return False
            x+=row[z];y+=col[z]
    return True

def nqueen(n,col,ans):
    if col>=n: return True
    for i in range(n):
        if is_safe(i,col,n,ans):
            ans[i][col]=1
            if nqueen(n,col+1,ans): return True
        ans[i][col]=0
    return False
#most optimal solution
ld=[0]*30
rd=[0]*30
column=[0]*30

def opt_nqueen(col,ans,n):
    if col>=n: return True
    for i in range(n):
        if ld[i-col+n-1]!=1 and rd[i+col]!=1 and column[i]!=1:
            ans[i][col]=1; ld[i-col+n-1]=1; rd[i+col]=1; column[i]=1
            if opt_nqueen(col+1,ans,n): return True
            ans[i][col]=0; ld[i-col+n-1]=0; rd[i+col]=0; column[i]=0
    #print(column)
    return False



"""
[[0, 0, 1, 0], 
 [1, 0, 0, 0], 
 [0, 0, 0, 1], 
 [0, 1, 0, 0]]

"""    
if __name__=="__main__":
    
    start_time = time.time()
    n=10
    grid=[[0]*n for i in range(n)]
    print(nqueen(n,0,grid))
    print(grid)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    start_time = time.time()
    nn=10
    ngrid=[[0]*nn for i in range(nn)]
    print(opt_nqueen(0,ngrid,nn))
    print(ngrid)
    print("--- %s seconds ---" % (time.time() - start_time))
    
