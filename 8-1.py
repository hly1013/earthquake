'''
Q.
A와 B는 각자 만든 영어 단어장에 같은 단어가 얼마나 있는지 확인하려고 한다.
두 사람이 만든 단어장에 공통으로 들어있는 단어의 개수를 알아내는 프로그램을 만드시오. 단, 모든 문자는 소문자로 되어 있다.

input.
T: 테스트 케이스의 개수 (1<=T<=50)
N: A의 단어개수 (3<=N,M<=3000)
M: B의 단어개수 
A의 단어들 (단어 길이는 20글자 이내)
B의 단어들
'''

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
            if len(word1) != len(word2): #길이가 다르면 같은 단어일리 없으므로
                continue
            for i in range(0, len(word1)): #길이 같으면 한글자씩 비교
                if word1[i] == word2[i]:
                    pass
                else:
                    break
            else: 
                count += 1
    
    print('#%d %d' %(test_case, count))