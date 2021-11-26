dic={}
for i in range(26):
    dic[str(i+1)]=chr(97+i)

def decoder(inp,out):
    if len(inp)==0:
        arr.append(out)
        return 
    try:
        out1=out+dic[inp[:1]]
        inp1=inp[1:]
        decoder(inp1,out1)
        if len(inp)>=2 and inp[:2] in dic:
            out2=out+dic[inp[:2]]
            inp2=inp[2:]
            decoder(inp2,out2)
    except:
        return 0

if __name__=="__main__":
    arr=[]
    s="70262"
    decoder(s,"")
    print(arr)
    print(len(arr))