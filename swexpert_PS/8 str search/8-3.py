'''
Q.
주어진 문자열의 부분 문자열을 사전순으로 정렬한 후, N번째 부분 문자열의 첫 글자와 글자 수를 출력

input.
T: 테스트 케이스의 개수 (1<=T<=50)
N (문자열의 길이 이내)
문자열 (길이는 4글자 이상 1000글자 이내)
'''
#실행시간 어떻게 더 줄이지?

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