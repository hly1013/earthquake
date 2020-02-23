'''
recursive function 'getsum(i, j)'
: min sum from 0,0 to i,j

called once per n x n table (i = 0, j = 0)
'''
def getsum(i, j): 
    if i == 0 :             # i == 0
        if j == 0 :
            s[i][j] = l[i][j]
            getsum(i+1, j), getsum(i, j+1)
        if j != 0 :
            s[i][j] = s[i][j-1] + l[i][j]
            getsum(i+1, j)
            if j < n-1 :
                getsum(i, j+1)
    else :                   # i != 0
        if j == 0 :
            s[i][j] = s[i-1][j] + l[i][j]
            getsum(i, j+1)
            if i < n-1 :
                getsum(i+1, j)
        if j != 0 :
            s[i][j] = (s[i-1][j] if s[i-1][j] < s[i][j-1] else s[i][j-1]) + l[i][j]
            if i < n-1 :
                getsum(i+1, j)
            if j < n-1 :
                getsum(i, j+1)
            if i == n-1 and j == n-1 : # end condition (of recursive function 'getsum')
                return s[i][j]      

'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    
    # 2차원 리스트 생성
    l = []              #for input
    s = []              #for getting sum

    for i in range(0, n):
        l.append([])
        s.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            l[i].append(int(temp[j]))
            s[i].append(0)

    # calling function 'getsum'
    getsum(0, 0)
    print('#%d %d' %(test_case, s[n-1][n-1]))