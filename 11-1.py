'''
N개의 서로 다른 자연수를 원소로 갖는 집합에서, 부분집합을 만들었다.
이때 원소 사이의 순서가 원래 집합에서의 순서와 일치하고, 오름 차순 정렬을 해도 원소의 순서가 바뀌지 않는 경우가 있다.
이 중 원소의 개수가 가장 많은 부분집합의 원소 개수를 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, 원소의 개수 N과 N개의 자연수 ai가 한 줄에 주어진다.
1<=T<=50, 1<=N, i<=1000, 1<=ai<=N

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
# => 최장 증가 수열 구하기와 동일!

#LIS[i]: a[i]로 끝나는 최장 증가 수열의 길이 저장
def LIS_DP(l):
    LIS = [0]*len(l)
    for i in range(0, len(l)):
        LIS[i] = 1
        for j in range(0, i):
            if l[j] < l[i] and 1 + LIS[j] > LIS[i]:
                LIS[i] = 1 + LIS[j]
    return max(LIS)


T = int(input())
for test_case in range(1, T + 1):
    l = list(input().split())
    l = list(map(int, l))
    l.pop(0)

    print('#%d %d' %(test_case, LIS_DP(l)))