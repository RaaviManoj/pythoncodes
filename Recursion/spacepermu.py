def spaces(inp,out):
    if len(inp)==0:
        arr.append(out)
        return 
    out1=out+" "+inp[:1]
    out2=out+inp[:1]
    inp=inp[1:]
    spaces(inp,out2)
    spaces(inp,out1)

if __name__=="__main__":
    s="abc"
    arr=[]
    spaces(s[1:],s[0])
    print(arr)