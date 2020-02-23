'''
is there any run or triplet?
'''
def isany(c):
    for i in range(0, 10):
        if c[i] == 3:
            return True
        if i <= 7:
            if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
                return True
    else:
        return False


'''
main function
'''
T = int(input())
for test_case in range(1, T + 1):
    #일단 한줄 입력받기
    l = list(input().split())
    l = list(map(int, l))

    #player1과 player2의 카드 따로 저장
    p1 = [] #player1's card picking list
    p2 = [] #player2's card picking list
    for i in range(0, 6):
        p1.append(l[2*i])
        p2.append(l[2*i+1])
    
    #누가 이길 것인가?!
    c1 = [0]*10 #count list for player 1's cards
    c2 = [0]*10 #count list for player 2's cards
    for i in range(0, 6):
        c1[p1[i]] += 1
        if isany(c1): 
            print('#%d %d' %(test_case, 1))
            break
        c2[p2[i]] += 1
        if isany(c2):
            print('#%d %d' %(test_case, 2))
            break
    else:
        print('#%d %d' %(test_case, 0))