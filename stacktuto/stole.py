arr = [2, 3, 3, 1, 2]
n = len(arr)


def stole(arr, n):
    s = []
    r = []
    for i in range(n):
        if len(s) == 0:
            r.append(-1)
        elif arr[i] > s[-1]:
            r.append(s[-1])
        elif arr[i] <= s[-1]:
            while(len(s) > 0 and arr[i] <= s[-1]):
                s.pop()
            if len(s) == 0:
                r.append(-1)
            elif arr[i] > s[-1]:
                r.append(s[-1])
        s.append(arr[i])
    return r


print(arr)
print(stole(arr, n))
