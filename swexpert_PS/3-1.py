'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    #n개의 화물
    N = list(input().split())
    N = list(map(int, N))

    #m개의 트럭
    M = list(input().split())
    M = list(map(int, M))

    #sorting N, M (descending order)
    N = sorted(N, reverse = True)
    M = sorted(M, reverse = True)

    sum = 0 # 총 나른 화물들의 총중량
    '''
    가장 큰 N부터 실어 나르기 시작
    각 N에 대해 가장 큰 M에서부터 고르기 시작
    '''
    for i in range(0, n):
        for j in range(0, m):
            if M[j] >= N[i]:
                sum += N[i]
                M[j] = 0
                break                   # "break"하지 않으면 한 화물이 중복되어 계산되는 오류 발생함
        else:
            continue
    
    print('#%d %d' %(test_case, sum))