B = {}

def init(n):
    if n in B:
        pass
    else:
        B[n] = [-1]*(n+1)
        B[n][0] = 1
        B[n][n] = 1


def bino(n, k):
    if k == 0 or k == n : return 1

    if n-1 in B:
        pass
    else: 
        init(n-1)

    if B[n][k] != -1 :
         return B[n][k]
    else:
        B[n][k] = bino(n-1, k-1) + bino(n-1, k)
        return B[n][k]

T = int(input())
for test_case in range(1, T+1):
    #get n, a, b
    n, a, b = map(int, input().split())
    
    init(n)

    if a < b:
        k = a
    else:
        k = b

    print('#%d %d' %(test_case, bino(n, k)))