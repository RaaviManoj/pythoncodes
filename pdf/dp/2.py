grid=[[1,2,3],[4,5,6]]
m=len(grid)
n=len(grid[0])
arr=[[-1 for i in range(n+1)]for j in range(m+1)]
def path(m,n):
    print(arr)
    if m<0 and n<0:
        return 0
    if arr[m][n]!=-1:
        return arr[m][n]
    if m==0 and n==0:
        return grid[0][0]
    elif m==0:
        arr[m][n]=path(m,n-1)+grid[m][n]
        return arr[m][n]
    elif n==0:
        arr[m][n]=path(m-1,n)+grid[m][n]
        return arr[m][n]
    else:
        arr[m][n]=min(path(m-1,n)+grid[m][n],path(m,n-1)+grid[m][n])
        return arr[m][n]
    

print( path(m-1,n-1))