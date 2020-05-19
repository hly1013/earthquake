T = int(input())
for test_case in range(1, T+1):
    #get input
    V, E = map(int, input().split())
    L = []
    for _ in range(0, E):
        l = list(input().split())
        l = list(map(int, l))
        L.append(l)
    
    #sort input(path)
    L = sorted(L, key = lambda l:l[2])

    #select path
    sum = 0
    visited = [0]*(V+1)
    for p in L:
        #if cycle, do not select
        if visited[p[0]] and visited[p[1]] :
            continue
        #if all node selected, stop selecting
        for i in range(0, V+1):
            if not visited[i] :
                break
        else:
            break
        #select
        visited[p[0]] = True
        visited[p[1]] = True
        sum += p[2]

    print('#%d %d' %(test_case, sum))