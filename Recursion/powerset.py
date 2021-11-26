def power_set(inp,out):
    if len(inp)==0:
        arr.append(out)
        return 
    out1=out+inp[:1]
    inp=inp[1:]
    power_set(inp,out)
    power_set(inp,out1)

if __name__=="__main__":
    s=[1,2,2]
    arr=[]
    power_set(s,[])
    print(sorted(arr,key=lambda x:len(x)))