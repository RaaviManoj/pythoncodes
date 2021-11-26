arr = [2, 3, 3, 1, 2]
n = len(arr)


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


print(arr)
print(stolein(arr, n))
