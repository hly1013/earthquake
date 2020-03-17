'''
checkindexout(x', y')
'''
def checkindexout(x_, y_):
    global n
    if x_ > n or y_ > n:
        return True
    else:
        return False

'''
checkpruning(cost)
'''
def checkpruning(cost):
    if cost >= min:
        return True
    else:
        return False

'''
checkcyle(x', y')
'''
def checkcycle(x_, y_):
    if (x_, y_) in visited:
        return True
    else:
        return False

'''
height((x, y), (x', y'))
'''
def height(x, y, x_, y_):
    if H[x_][y_] > H[x][y]:
        return H[x_][y_] - H[x][y]
    else:
        return 0

'''
function in expand(x, y),
_expand(x', y')
'''
def _expand(x, y, x_, y_, c):
    cost = c
    if checkcycle(x_, y_) == False and checkpruning(cost) == False and checkindexout == False:
        visited.append((x_, y_))
        cost += 1 + height(x, y, x_, y_)
        return expand(x_, y_, c)


'''
secondary main function,
expand(x, y)
'''
def expand(x, y, c):
    global min, n
    if x == n and y == n: #종결 조건
        if c < min:
            min = c
    if x == 0:
        if y == 0:
            _expand(x, y, x, y+1, c)
            _expand(x, y, x+1, y, c)
        else: # y != 0
            _expand(x, y, x, y-1, c)
            _expand(x, y, x+1, y, c)
            _expand(x, y, x, y+1, c)
    else: # x != 0
        if y == 0:
            _expand(x, y, x-1, y, c)
            _expand(x, y, x, y+1, c)
            _expand(x, y, x+1, y, c)
        else: # y != 0
            _expand(x, y, x, y-1, c)
            _expand(x, y, x-1, y, c)
            _expand(x, y, x, y+1, c)
            _expand(x, y, x+1, y, c)

'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    #height table input H
    H = [] 
    for i in range(0, n):
        H.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            H[i].append(int(temp[j]))

    #
    min = 9999999 #maximum value for int
    cost = 0 #
    visited = [(0, 0)]
    expand(0, 0, 0)

    print('#%d %d' %(test_case, min))