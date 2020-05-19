def getmax(n, l):
    if l == [] or n == 0:
        return 0

    #
    if len(l) == 1:
        if n <= l[0][0]:
            return l[0][1]
        else:
            return 0


    c1 = getmax(n, l[:-2])
    c2 = getmax(n-l[-1][0], l[:-2]) + l[-1][1]
    return c1 if c1 > c2 else c2



T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    l = [] 
    for i in range(0, m):
        l.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, 2):
            l[i].append(int(temp[j]))

    print('#%d %d' %(test_case, getmax(n, l)))