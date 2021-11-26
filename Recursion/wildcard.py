def wild_match(p,s,i,j,n,m):
    print(i,j,n,m)
    if i>n or j>m: return False

    if i==n:
        print("hi")
        return j==m

    if i==n-1 and p[i]=='*':
        return True

    if j<m and p[i]==s[j] or p[i]=='?':
        return wild_match(p,s,i+1,j+1,n,m)

    if p[i]=='*':
        cond1=wild_match(p,s,i+1,j,n,m)
        cond2=wild_match(p,s,i,j+1,n,m)
        return cond1 or cond2
    
    if j<m and p[i]!=s[j]: return False

if __name__=="__main__":
    p="a*c?b"
    s="acdcb"
    n=len(p)
    m=len(s)
    print(wild_match(p,s,0,0,n,m))