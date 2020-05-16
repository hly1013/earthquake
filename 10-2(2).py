'''
1부터 N까지 양의 정수를 원소로 갖는 집합
모든 부분 집합에 대해 원소의 합이 K인 경우의 수 M

이미 부분 집합에 포함시킨 원소의 합 S와 아직 고려하지 않은 숫자들의 합 R을 동시에 활용하면 시간을 단축할 수 있다
이를 활용해 M을 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, N과 K가 주어진다.
( 3<=N<=100, 6<=K<=모든 원소의 합 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
# n: 이번에 고려해야 하는 숫자 (내림차순으로 고려), r: 아직 고려하지 않은 숫자들의 합, s: 이미 부분집합에 포함시킨 원소의 합
def iter(n, r, s): 
    global M, N, K

    if s > K:
        return
    if s + r < K:
        return
    if s == K:
        M += 1
        return
    
    iter(n-1, r-n, s+n)
    iter(n-1, r-n, s)



T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    #initialize
    S = 0
    R = N*(N+1)/2 #summation of 1, 2, ... , N
    M = 0
    
    iter(N, R, S)

    print('#%d %d' %(test_case, M))