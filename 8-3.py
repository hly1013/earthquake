'''
실행시간 어떻게 더 줄이지?
'''

T = int(input())
for test_case in range(1, T + 1):
    #get input
    N, word = input().split()
    N = int(N)

    #get substring of word
    L = []
    for i in range(0, len(word)):
        for j in range(0, len(word)-i):
            #word idx; ith ~ (len(word)-1)th
            string = word[i:i+j+1]
            if string in L:
                pass
            else:
                L.append(string)
    
    #sort substring list L
    L = sorted(L, reverse = False)

    #output
    print('#%d %c %d' %(test_case, L[N-1][0], len(L[N-1])))