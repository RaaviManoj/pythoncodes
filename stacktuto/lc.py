
nums = [2, 3, 3, 1, 2]
mod = 10**9+7
n = len(nums)

pre = [0]
for i in range(n):
    pre.append(pre[-1]+nums[i])


def stolein(arr, n):
    s = []
    r = []
    for i in range(n):
        if len(s) == 0:
            r.append(-1)
        elif arr[i] > s[-1][0]:
            r.append(s[-1][1])
        elif arr[i] <= s[-1][0]:
            while(len(s) > 0 and arr[i] <= s[-1][0]):
                s.pop()
            if len(s) == 0:
                r.append(-1)
            elif arr[i] > s[-1][0]:
                r.append(s[-1][1])
        s.append([arr[i], i])
    return r


def storin(arr, n):
    s = []
    r = []
    for i in range(n-1, -1, -1):
        if len(s) == 0:
            r.append(n)
        elif arr[i] > s[-1][0]:
            r.append(s[-1][1])
        elif arr[i] <= s[-1][0]:
            while(len(s) > 0 and arr[i] <= s[-1][0]):
                s.pop()
            if len(s) == 0:
                r.append(n)
            elif arr[i] > s[-1][0]:
                r.append(s[-1][1])
        s.append([arr[i], i])
    return r[::-1]


l = stolein(nums, n)

r = storin(nums, n)
#print(pre, l, r)
res = 0
for i in range(n):
    #print(i, res)
    if l[i] == -1 and r[i] == n:
        val = nums[i]*(pre[n]-pre[0])
        res = max(res, val)
    elif l[i] == -1:
        q = r[i]
        p = 0
        val = nums[i]*(pre[q]-pre[p+1])
        res = max(res, val)
    elif r[i] == n:
        p = l[i]
        val = nums[i]*(pre[n]-pre[p+1])
        res = max(res, val)
    else:
        val = nums[i]*(pre[r[i]]-pre[l[i]+1])
        res = max(res, val)
    #print(i, val)
print(res)
