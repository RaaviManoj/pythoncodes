def bina(l,r,n,out):
    if l+r==n:
        arr.append(out)
        return
    if r<l:
        bina(l,r+1,n,out+"0")
    bina(l+1,r,n,out+"1")

if __name__=="__main__":
    arr=[]
    bina(0,0,5,"")
    print(arr)