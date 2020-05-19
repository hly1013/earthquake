#시간초과 뜰듯

'''
main function
'''
import math

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    #2차원 리스트 생성
    V = [] #idx i, j: i->j 때의 소비량
    for i in range(0, n):
        V.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            V[i].append(int(temp[j]))
    
    min = math.inf
    getMinCost()

    print('#%d %d' %(test_case, min))


def getMinCost():
    global N, V, min




