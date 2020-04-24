def iter(n, r, s):
    global K, c

    #탐색 종료 조건
    if s == K:
        c += 1
        return
    if n == 0:
        return

    if r - n == K - s:
        c += 1
        return
    elif r - n < K - s:
        #pruning
        if r < K - s:
            return
        iter(n-1, r-n, s+n)
    else: # r - n > K - s
        iter(n-1, r-n, s)
        iter(n-1, r-n, s+n)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    #initialize
    S = 0
    R = N*(N+1)/2 #summation of 1, 2, ... , N
    c = 0
    
    iter(N, R, S)

    print('#%d %d' %(test_case, c))