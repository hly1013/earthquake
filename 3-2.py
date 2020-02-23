'''
for sorting in main function
'''
def take_second(elem):
    return elem[1]

'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) 

    # n개의 경우에 대해 s, e 저장
    se = []
    for i in range(1, n+1):
        s, e = map(int, input().split())
        se.append([s, e])
    
    #sorting se; key: e, ascending order
    se = sorted(se, key = take_second)

    sum = 0 # 도크 쓸 수 있는 총 횟수
    temp = se[0][1]
    sum += 1
    for i in range(1, n):
        if se[i][0] >= temp:
            temp = se[i][1]
            sum += 1
    
    print('#%d %d' %(test_case, sum))