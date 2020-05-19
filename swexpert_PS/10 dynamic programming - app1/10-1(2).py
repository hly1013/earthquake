'''
크기가 정해진 박스가 가득 찰 때까지 마음대로 물건을 골라 담을 수 있는 해피박스
박스에 담긴 물건의 가격합계가 최대가 되도록
남은 물건의 크기와 가격이 주어질 때, A씨가 담을 수 있는 물건 가격은 최대 얼마인지 알아내는 프로그램

[입력]
첫 줄에 테스트 케이스의 개수 T
테스트 케이스 별로, 첫 줄에 박스의 크기 N과 상품의 개수 M
이후 M개의 줄에 걸쳐 상품 i의 크기Si와 가격Pi
10<=N<=100, 1<= Si, Pi, M<=20

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''

# n: 남은 무게, i: 탐색해야 하는 아이템 idx #, p: 담은 아이템 가격 총합
def getmax(n, i, p):
    global max, I, l

    if i < l:
        si = I[i][0]
        pi = I[i][1]
        i += 1
        if n >= si:
            getmax(n-si, i, p+pi)
        getmax(n, i, p)
    else: # 다 탐색한 경우
        if p > max:
            max = p


T = int(input())
for test_case in range(1, T + 1):
    # N: box size, M: item #
    N, M = map(int, input().split())

    # (Si, Pi) list I
    I = [] 
    for i in range(0, M):
        I.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, 2):
            I[i].append(int(temp[j]))

    l = len(I)
    max = 0
    getmax(N, 0, 0)

    print('#%d %d' %(test_case, max))