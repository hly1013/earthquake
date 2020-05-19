'''
route list a, battery usage list l
get battery usage sum using l
i: idx variable of route list 'a'
'''
def getsum(a):
    s = 0 #battery usage sum
    i = 0

    # i == 0 : start
    s += l[0][a[i]]

    # 1 <= i <= n-2 : middle
    for i in range(1, n-1): 
        s += l[a[i-1]][a[i]]

    # i == n-2: end
    else: s += l[a[i]][0] 
    return s

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
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) #n개의 state

  #2차원 리스트 생성
    l = [] # l[i][j]: state# i->j 때의 소비량
    for i in range(0, n):
        l.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            l[i].append(int(temp[j]))
    
    #루트 저장할 list a (start, end point: 1)
    a = []
    for i in range(1, n): 
        a.append(i) # a = [1, ... , n-1] # route except start point, end point (both are 0)

    p = perm(a)
    s = 10000
    for i in range(len(p)):
        temp = getsum(p[i])
        if temp < s :
            s = temp

    print('#%d %d' %(test_case, s))