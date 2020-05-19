'''
Q.
문자열 그룹 A와 B가 주어질 때, B에 속한 문자열 중 A의 접두어인 문자열의 개수를 알아내는 프로그램을 만드시오. 
모든 단어는 소문자로 이루어져 있다.

input.
T: 테스트 케이스의 개수 (1<=T<=50)
N: A의 단어 개수 (3<=N,M<=3000)
M: B의 단어 개수
A의 단어들 (단어의 길이는 20글자 이내)
B의 단어들
'''

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
            if len(word) < len(prefix): #단어의 길이보다 긴 문자열은 그 단어의 접두어일 수 없음
                continue
            for i in range(0, len(prefix)):
                if word[i] == prefix[i]:
                    pass
                else:
                    break
            else: #접두어임을 확인 완료!
                if prefix in pre:
                    pass
                else:
                    pre.append(prefix)
                    count += 1
    
    print('#%d %d' %(test_case, count))