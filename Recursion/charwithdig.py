def spaces(inp,out):
    if len(inp)==0:
        arr.append(out)
        return 
    if inp[:1].isalpha():
        out1=out+inp[:1].upper()
        out2=out+inp[:1]
        inp=inp[1:]
        spaces(inp,out2)
        spaces(inp,out1)
    else:
        out1=out+inp[:1]
        inp=inp[1:]
        spaces(inp,out1)

if __name__=="__main__":
    s="a1b2c"
    arr=[]
    spaces(s,"")
    print(arr)