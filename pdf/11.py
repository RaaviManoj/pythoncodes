le=[1,2,3,4,5,6,7,8]
pr=[3,5,8,9,10,17,17,20]
tl=8
n=len(le)
dp=[[-1 for i in range(tl+1)]for j in range(n+1)]
def mapr(n,tl):
    if n==-1:
        return 0
    if tl==0:
        return 0
    if dp[n][tl]!=-1:
        return dp[n][tl]
    if tl>=le[n]:
        dp[n][tl]=max(mapr(n,tl-le[n])+pr[n],mapr(n-1,tl))
        return dp[n][tl]
    else:
        dp[n][tl]=mapr(n-1,tl)
        return dp[n][tl]
print(mapr(n-1,tl))