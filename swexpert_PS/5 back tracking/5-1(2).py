#왜안되냐

def whereToCharge(cnt, now, batt):
    global M, N, min

    if cnt >= min: #pruning
        return 

    if now == N: # end condition
        if cnt < min:
            min = cnt
        return
    
    if batt >= 1:
        whereToCharge(cnt, now+1, batt-1)
    whereToCharge(cnt+1, now+1, batt-1+M[now])


'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    M = list(input().split())
    M = list(map(int, M))
    N = M[0]

    min = N-2 # initial value

    whereToCharge(0, 2, M[1]-1)

    print('#%d %d' %(test_case, min))