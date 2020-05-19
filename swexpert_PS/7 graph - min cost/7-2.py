T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    #height table input H
    H = [] 
    for i in range(0, n):
        H.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            H[i].append(int(temp[j]))
    
    #minimum cost table C
    C = [[1000000]*n]*n
    for i in range(0, n):
        for j in range(0, n):
            #start node; cost = 0
            if i == 0 and j == 0:
                C[i][j] = 0
            else: 
                if i == 0: # j != 0
                    temp = (C[i][j-1] + 1 + (H[i][j]-H[i][j-1] if H[i][j]>H[i][j-1] else 0))
                    if temp < C[i][j]:
                        C[i][j] = temp
                elif j == 0: # i != 0
                    temp = (C[i][j-1] + 1 + (H[i][j]-H[i-1][j] if H[i][j]>H[i-1][j] else 0))
                    if temp < C[i][j]:
                        C[i][j] = temp
                else: # i != 0 and j != 0
                    h1 = H[i][j]-H[i][j-1] 
                    h2 = H[i][j]-H[i-1][j]
                    if h1 < h2:
                        temp = (C[i][j-1] + 1 + (h1 if h1 > 0 else 0))
                    else:
                        temp = (C[i][j-1] + 1 + (h2 if h2 > 0 else 0))
                    if temp < C[i][j]:
                        C[i][j] = temp

    print(C)
    #print minimum cost to destination node
    print('#%d %d' %(test_case, C[n-1][n-1]))