T = int(input())
for test_case in range(1, T+1):
    #get input (path info list P)
    N, E = map(int, input().split())
    P = []
    for _ in range(0, E):
        l = list(input().split())
        l = list(map(int, l))
        P.append(l)
    
    #sort input(path)
    P = sorted(P, key = lambda l:l[0])

    #minimum cost list C
    C = [10000000]*(N+1) #init value: infinity
    C[0] = 0 #initial node; cost = 0
    for p in P:
        s = p[0]
        e = p[1]
        w = p[2]

        if C[e] > C[s] + w:
            C[e] = C[s] + w #update min cost
        
    #print minimum cost to destination node
    print('#%d %d' %(test_case, C[N]))
        
