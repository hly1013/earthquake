#그래프라기보다는... 그냥 무작정 한 코드
#=>효율 안좋음
#그래프로 어떻게 하지?

'''
getmin(n, m)
'''
def getmin(n, m, c): #n: current node, m: target node, c: path length
    global min
    
    if n == m: #end condition
        if min > c:
            min = c
        return min

    if n > 1000000: #non-promising condition 1
        return
    if c > min: #non-promising condition 2
        return 

    
    if n < m: #n-1, n-10 연산이 필요 없는 경우
        getmin(n+1, m, c+1)
        getmin(n*2, m, c+1)
    if n - m > 10: #n-1보다 n-10이 효율 좋은 경우
        pass
    else:
        getmin(n-1, m, c+1)
    
    getmin(n-10, m, c+1)
    '''
    getmin(n+1, m, c+1)
    getmin(n*2, m, c+1)
    getmin(n-1, m, c+1)
    getmin(n-10, m, c+1)
    '''
    
    return min #final result


'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    min = 1000000
    result = getmin(N, M, 0)

    print('#%d %d' %(test_case, result))
