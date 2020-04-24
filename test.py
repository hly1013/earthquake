T = int(input())
for test_case in range(1, T + 1):
    N = list(input().split())
    N = list(map(int, N))
    N.pop(0)

    print(N)