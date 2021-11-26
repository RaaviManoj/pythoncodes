n=10

def tower(n,s,d,h):
    if n==1:
        print("moving "+str(n)+" from "+s+" to "+d)
        return 
    tower(n-1,s,h,d)
    print("moving "+str(n)+" from "+s+" to "+d)
    tower(n-1,h,d,s) 
tower(n,'s','d','h')