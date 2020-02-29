'''
l: 표
loc: 현재 정류장 번호
charge: 현재 충전상태
n: 충전 횟수
'''
def wheretoCharge(l, loc, charge, n = 0):
    global min, N
    if N <= loc+charge: #can reach to destination
        if n < min:          #minimun charge # ?
            min = n
            return
    for i in range(loc+1, loc+charge+1): #cannot reach to destination yet
        if n >= min:          #non-promising-> return
            return 
        if i <= N-1:
            wheretoCharge(l, i, charge - (i - loc) + l[i-1], n+1)

'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    M = list(input().split())
    M = list(map(int, M))
    N = M.pop(0)

    charge = M[0]
    min = N-2
    wheretoCharge(M, 1, charge)

    print('#%d %d' %(test_case, min))