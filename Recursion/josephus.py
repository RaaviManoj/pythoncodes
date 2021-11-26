from collections import deque

def final_one(index,k,arr):
    if len(arr)==1:
        return arr[0]
    index=(index+k)%len(arr)
    del arr[index]
    return final_one(index,k,arr)

if __name__=="__main__":
    n=400;k=7
    arr=[i for i in range(1,n+1)]
    qu=deque(arr)
    print(final_one(0,k-1,qu))