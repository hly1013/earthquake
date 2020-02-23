T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    #n개의 화물
    N = list(input().split())
    N = list(map(int, N))

    #m개의 트럭
    M = list(input().split())
    M = list(map(int, M))