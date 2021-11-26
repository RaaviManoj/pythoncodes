arr = [2, 3, 3, 1, 2]
n = len(arr)


def stori(arr, n):
    s = []
    r = []
    for i in range(n-1, -1, -1):
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
    return r[::-1]


print(arr)
print(stori(arr, n))
