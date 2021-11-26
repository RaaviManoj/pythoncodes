def spaces(l,r,out):
    if l==0 and r==0:
        arr.append(out)
        return 
    if r>l:
        spaces(l,r-1,out+")")
    if l>0:
        spaces(l-1,r,out+"(")


if __name__=="__main__":
    arr=[]
    spaces(3,3,"")
    print(arr)