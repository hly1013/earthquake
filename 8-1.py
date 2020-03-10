T = int(input())
for test_case in range(1, T+1):
    #get N, M
    N, M = map(int, input().split())
    #get words of A, B
    A = []
    for _ in range(0, N):
        l = input()
        A.append(l)
    B = []
    for _ in range(0, M):
        l = input()
        B.append(l)

    #count common words
    count = 0
    for word1 in A:
        for word2 in B:
            if len(word1) != len(word2):
                continue
            for i in range(0, len(word1)):
                if word1[i] == word2[i]:
                    pass
                else:
                    break
            else: 
                count += 1
    
    print('#%d %d' %(test_case, count))