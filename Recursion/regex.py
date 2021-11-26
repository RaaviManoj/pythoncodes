def matcher(p,s,i,j,n,m):
    if i>n or j>m: return False

    if i==n: return j==m

    flag=False
    if j<m and p[i]==s[j] or p[i]=='.': flag=True

    if i<n-1 and p[i+1]=='*':
        cond1=matcher(p,s,i+2,j,n,m)
        cond2=flag and matcher(p,s,i,j+1,n,m)
        return cond1 or cond2
    
    else:
        return flag and matcher(p,s,i+1,j+1,n,m)

if __name__=="__main__":
    p="a*"
    s="aa"
    n=len(p)
    m=len(s)
    print(matcher(p,s,0,0,n,m))