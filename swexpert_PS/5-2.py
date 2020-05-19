'''
파이썬의 라이브러리를 활용한 순열:
import itertools
mylist = [1, 2, 3]
result = itertools.permutations(mylist) #(mylist, 3)
				# r 생략시 기본값 리스트크기
print(list(result))
'''
import itertools
def perm(a):
    result = itertools.permutations(a)
    return(list(result))

'''
get_min(cost)
'''
import math
def get_min(cost):
    min = 0
    for i in range(0, n):
        min += cost[i][i]
    global n

    #idx array, l
    l = []
    for i in range(0, n):
        l.append(i)
    
    #all possibile idx seq
    l_perm = perm(l)

    #back-tracking
    for i in range(0, math.factorial(n)-1):
        sum = 0
        idx = 0
        for j in l_perm[i]:
            #non-promising condition (breakpoint)
            if sum > min:
                break

            sum += cost[idx][j]
            idx += 1
        else: 
            if sum < min:
                min = sum

    #min: minimum cost
    return min



'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    #2차원 리스트 생성
    cost = [] #idx i, j: i->j 때의 소비량
    for i in range(0, n):
        cost.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            cost[i].append(int(temp[j]))
    
    result = get_min(cost)

    print('#%d %d' %(test_case, result))