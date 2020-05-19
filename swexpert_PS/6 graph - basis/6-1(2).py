'''
from lecture, 
graph functions
'''
'''
Q. 
how to add new keys to dictionary?
A.
d = {'key': 'value'}
print(d)
# {'key': 'value'}
d['mynewkey'] = 'mynewvalue'
print(d)
# {'key': 'value', 'mynewkey': 'mynewvalue'}
'''
'''
p: dictionary; {current node : parent node}
rank: dictionary; {current node : rank of subgraph}
'''

#make-set
def make_set(x):
    p[x] = x
    rank[x] = 0

#find-set
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

#union
def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1
def union(x, y):
    link(find_set(x), find_set(y))



'''
makegraph(N, M)
'''
def makegraph(N, M):
    make_set(N)
    make_set('+1')
    make_set('-1')
    make_set('*2')
    make_set('-10')




'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    #make graph
    makegraph(N, M)

    #get min
    min = 1000000
    result = getmin(N, M, 0) #-> getmin(graph, M)

    print('#%d %d' %(test_case, result))
