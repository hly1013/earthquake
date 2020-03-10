T = int(input())
for test_case in range(1, T+1):
    #get N, M
    N, M = map(int, input().split())
    #get string of A, B
    A = []
    for _ in range(0, N):
        l = input()
        A.append(l)
    B = []
    for _ in range(0, M):
        l = input()
        B.append(l)

    #count prefixes
    pre = []
    count = 0
    for word in A:
        for prefix in B:
            if len(word) < len(prefix):
                continue
            for i in range(0, len(prefix)):
                if word[i] == prefix[i]:
                    pass
                else:
                    break
            else: 
                if prefix in pre:
                    pass
                else:
                    pre.append(prefix)
                    count += 1
    
    print('#%d %d' %(test_case, count))