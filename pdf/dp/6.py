coi=[1,2,5,10,20,50,100,200]
n=len(coi)
c=200
dp=[[-1 for i in range(c+1)]for j in range(n)]
def chan(n,c):
    if n==-1:
        return 0
    if c==0:
        return 1
    if(coi[n]<=c):
        dp[n][c]=chan(n,c-coi[n])+chan(n-1,c)
        return dp[n][c]
    else:
        dp[n][c]=chan(n-1,c)
        return dp[n][c]
    
print(chan(n-1,c))
